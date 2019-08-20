import jwt
import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
from backend.utils.response import Response
from backend.utils.errors import ErrorResponse
from backend.models.user import User
from backend.schemas.errors import (
    PayloadNotFound,
    JsonNotFound,
    UserNotFound
)
from backend.schemas.token import TokenSchema
from backend.models.token import ResetPasswordToken
from psycopg2 import ProgrammingError

router = Blueprint('resetUser', __name__)


@router.route('/password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if data and data['username']:
        user = User.getUser(username=data['username'])
        expire = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        token = jwt.encode({
            'id': user.username,
            'exp': expire
        }, app.config.get('SECRET_KEY'))
        return jsonify(
            Response(200).generateResetURL(
                token.decode('UTF-8')))
    else:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()


@router.route('/token', methods=['POST'])
def pwd_reset_token():
    data = request.get_json()['data']['attributes']
    if 'email' not in data.keys():
        print('Email not found')
    email = data['email']
    user = User.getUser(email=email)
    if not user:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    token = jwt.encode({
        'id': user.id,
        'exp': expire
    }, app.config.get('SECRET_KEY'))
    try:
        resetObj = ResetPasswordToken.query.get(user.id)
        resetObj.token = token
    except ProgrammingError:
        resetObj = ResetPasswordToken(user.id, token.decode('UTF-8'))

    resetObj.save_to_db()
    return jsonify(TokenSchema().dump(resetObj).data)
