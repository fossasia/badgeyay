from flask import Blueprint, jsonify, request
from firebase_admin import auth
from api.models.user import User
from api.models.permissions import Permissions
from api.config.config import admins
from api.utils.update_user import update_firebase_username
from api.schemas.user import (
    UserSchema,
    OAuthUserSchema,
    FTLUserSchema,
    PermissionSchema
)


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

        if user.email in admins:
            newUser.siteAdmin = True

        newUser.save_to_db()

        perm = Permissions(isUser=True, user_permissions=newUser)
        perm.save_to_db()

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
            if data['email'] in admins:
                newUser.siteAdmin = True
            newUser.save_to_db()
            perm = Permissions(isUser=True, user_permissions=newUser)
            perm.save_to_db()
        else:
            newUser = user_
        return jsonify(schema.dump(newUser).data)


@router.route('/permission', methods=['GET'])
def user_permissions():
    args = request.args
    if 'id' in args.keys():
        perm = Permissions.getPermissions(args['id'])
        return jsonify(PermissionSchema().dump(perm).data)


@router.route('/register/<uid>', methods=['PATCH'])
def patchUser(uid):
    data = request.get_json()['data']['attributes']
    user = User.getUser(user_id=uid)
    if 'ftl' in data.keys():
        user.ftl = data['ftl']
        user.save_to_db()

    if 'username' in data.keys():
        user.username = data['username']
        update_firebase_username(user.id, user.username)
        user.save_to_db()

    return jsonify(FTLUserSchema().dump(user).data)
