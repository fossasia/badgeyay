import datetime
import jwt


from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response
from api.utils.errors import ErrorResponse
from api.schemas.errors import (
    PayloadNotFound,
    OperationNotFound
)


router = Blueprint('oAuthToken', __name__)


@router.route('/oauth_token', methods=['POST'])
def oauth_token():
    try:
        data = request.get_json()
        uid = data['uid']
    except Exception:
        return ErrorResponse(PayloadNotFound(uid).message, 422, {'Content-Type': 'application/json'})

    try:
        token = jwt.encode(
            {'user': data.get('username'),
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
            app.config.get('SECRET_KEY'))

    except Exception:
        return ErrorResponse(OperationNotFound(uid).message, 422, {'Content-Type': 'application/json'})

    return jsonify(
        Response(200).generateToken(
            token.decode('UTF-8')))
