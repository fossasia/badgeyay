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
    except Exception:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if 'name' in data.keys():
        user = User.getUser(username=data['name'])
        uid = data['uid']
        if not user:
            return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

        if not verifyPassword(user, data['password']):
            return ErrorResponse(PasswordNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

        token = jwt.encode(
            {'user': user.username,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
            app.config.get('SECRET_KEY'))

        return jsonify(
            Response(200).generateToken(
                token.decode('UTF-8')))

    return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()


@router.route('/get_user', methods=['GET'])
def index():
    data = request.args
    user = User.getUser(username=data.get('username'))
    schema = UserSchema()
    return jsonify(schema.dump(user).data)
