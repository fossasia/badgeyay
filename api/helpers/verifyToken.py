import jwt
from functools import wraps
from flask import request, jsonify
from flask import current_app as app
from api.schemas.errors import (
    PayloadNotFound,
    AdminNotFound
)
from api.utils.errors import ErrorResponse
from api.utils.response import Response


def loginRequired(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify(
                Response(403).generateMessage(
                    'No token has been specified'))

        try:
            jwt.decode(token, app.config['SECRET_KEY'])
        except Exception as e:
            return jsonify(
                Response(403).generateMessage(
                    str(e)))

        return func(*args, **kwargs)

    return decorated


def adminRequired(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            if 'adminStatus' in data.keys():
                return func(*args, **kwargs)
            return ErrorResponse(AdminNotFound().message, 422, {'Content-Type': 'application/json'})
        except Exception as e:
            print(e)

    return decorated
