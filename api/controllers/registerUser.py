from flask import Blueprint, jsonify, request
from firebase_admin import auth
from werkzeug.security import generate_password_hash
from api.models.user import User
from api.schemas.errors import FirebaseError
from api.utils.errors import ErrorResponse
from api.models.permissions import Permissions
from api.config.config import admins
from api.utils.update_user import (
    update_firebase_username,
    update_firebase_password
)
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
        try:
            user = auth.create_user(
                email=data['email'],
                email_verified=False,
                password=data['password'],
                display_name=data['username'],
            )
        except auth.AuthError as e:
            if e.code == 'USER_CREATE_ERROR':
                errmsg = 'User with email already exists'
            return ErrorResponse(FirebaseError(errmsg).message, 422, {'Content-Type': 'application/json'}).respond()

        newUser = User(
            id_=user.uid,
            username=data['username'],
            email=user.email,
            password=data['password'])

        if user.email in admins:
            newUser.siteAdmin = True

        newUser.save_to_db()

        if newUser.email in admins:
            perm = Permissions(isUser=True, isAdmin=True, user_permissions=newUser)
            perm.save_to_db()
        else:
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
                password=data['password'],
                photoURL=data['photoURL']
            )
            if data['email'] in admins:
                newUser.siteAdmin = True
            newUser.save_to_db()

            if newUser.email in admins:
                perm = Permissions(isUser=True, isAdmin=True, user_permissions=newUser)
                perm.save_to_db()
            else:
                perm = Permissions(isUser=True, user_permissions=newUser)
                perm.save_to_db()
        else:
            newUser = user_
        return jsonify(schema.dump(newUser).data)


@router.route('/permission', methods=['GET'])
def user_permissions():
    args = request.args
    if 'id' in args.keys():
        perm = Permissions.get_by_uid(args['id'])
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

    if 'password' in data.keys() and data['password'] is not None:
        update_firebase_password(user.id, data['password'])
        user.password = generate_password_hash(data['password'])
        user.save_to_db()

    return jsonify(FTLUserSchema().dump(user).data)
