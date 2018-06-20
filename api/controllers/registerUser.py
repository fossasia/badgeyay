from flask import Blueprint, jsonify, request
from firebase_admin import auth
from api.models.user import User
from api.schemas.user import (
    UserSchema,
    OAuthUserSchema,
    FTLUserSchema
)
from api.helpers.verifyToken import loginRequired


router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def register_user():
    schema = UserSchema()
    input_data = request.get_json()
    if 'uid' not in input_data['data']['attributes'].keys():
        data, err = schema.load(input_data)
        if err:
            return jsonify(err)
        user = auth.create_user(
            email=data['email'],
            email_verified=False,
            password=data['password'],
            display_name=data['username'],
        )

        newUser = User(
            id_=user.uid,
            username=data['username'],
            email=user.email,
            password=data['password'])

        newUser.save_to_db()

        return jsonify(schema.dump(newUser).data)
    else:
        schema = OAuthUserSchema()
        data, err = schema.load(input_data)
        if err:
            return jsonify(err)

        uid = input_data['data']['attributes']['uid']
        user_ = User.getUser(user_id=uid)
        if not user_:
            newUser = User(
                id_=uid,
                username=data['username'],
                email=data['email'],
                password=None,
                photoURL=data['photoURL']
            )
            newUser.save_to_db()
        else:
            newUser = user_
        return jsonify(schema.dump(newUser).data)


@loginRequired
@router.route('/register/<uid>', methods=['PATCH'])
def patchUser(uid):
    data = request.get_json()['data']['attributes']
    user = User.getUser(user_id=uid)
    if 'ftl' in data.keys():
        user.ftl = data['ftl']
    user.save_to_db()
    return jsonify(FTLUserSchema().dump(user).data)
