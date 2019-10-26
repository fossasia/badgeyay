import jwt
from flask import Blueprint, jsonify, request
from flask import current_app as app
from backend.utils.response import Response
from backend.utils.errors import ErrorResponse
from backend.schemas.errors import (
    PayloadNotFound,
    OperationNotFound
)

router = Blueprint('oAuthToken', __name__)

@router.route('/oauth_token', methods=['POST'])
def oauth_token():
    try:
        data = request.get_json()
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    try:
        token = jwt.encode(
            {'user': data.get('username')},
            app.config.get('SECRET_KEY'))

    except Exception:
        return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    return jsonify(
        Response(200).generateToken(
            token.decode('UTF-8')))
