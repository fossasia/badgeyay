import jwt
import datetime

from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response
from api.helpers.verifyPassword import verifyPassword
from api.models.user import User
from api.schemas.user import UserSchema
from api.utils.errors import ErrorResponse
from api.schemas.errors import (
    JsonNotFound,
    UserNotFound,
    OperationNotFound,
    PasswordNotFound
)


router = Blueprint('loginUser', __name__)


@router.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        uid = data['uid']
    except Exception:
        return ErrorResponse(JsonNotFound(uid).message, 422, {'Content-Type': 'application/json'})

    if 'name' in data.keys():
        user = User.getUser(username=data['name'])
        if not user:
            return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'})

        if not verifyPassword(user, data['password']):
            return ErrorResponse(PasswordNotFound(uid).message, 422, {'Content-Type': 'application/json'})

        token = jwt.encode(
            {'user': user.username,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
            app.config.get('SECRET_KEY'))

        return jsonify(
            Response(200).generateToken(
                token.decode('UTF-8')))

    return ErrorResponse(OperationNotFound(uid).message, 422, {'Content-Type': 'application/json'})


@router.route('/get_user', methods=['GET'])
def index():
    data = request.args
    user = User.getUser(username=data.get('username'))
    schema = UserSchema()
    return jsonify(schema.dump(user).data)
