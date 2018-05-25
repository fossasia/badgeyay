import jwt
from functools import wraps
from flask import request, jsonify
from flask import current_app as app
from api.utils.response import Response


def loginRequired(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify(
                Response(403).generateErrorMessage(
                    'No token has been specified', 'token error'))

        try:
            jwt.decode(token, app.config['SECRET_KEY'])
        except Exception as e:
            return jsonify(
                Response(403).generateErrorMessage(
                    str(e), 'error'))

        return func(*args, **kwargs)

    return decorated
