import jwt
import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response
from api.utils.errors import ErrorResponse
from api.models.user import User
from api.schemas.errors import (
    PayloadNotFound,
    JsonNotFound
)


router = Blueprint('resetUser', __name__)


@router.route('/password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
        uid = data['uid']
    except Exception:
        return ErrorResponse(PayloadNotFound(uid).message, 422, {'Content-Type': 'application/json'})

    if data and data['username']:
        user = User.getUser(data['username'])
        expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
        token = jwt.encode({
            'id': user.username,
            'exp': expire
        }, app.config.get('SECRET_KEY'))
        return jsonify(
            Response(200).generateResetURL(
                token.decode('UTF-8')))
    else:
        return ErrorResponse(JsonNotFound(uid).message, 422, {'Content-Type': 'application/json'})
