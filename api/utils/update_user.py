from firebase_admin import auth
from flask import jsonify, make_response
from werkzeug.security import generate_password_hash

from api.utils.errors import ErrorResponse
from api.models.user import User
from api.schemas.errors import OperationNotFound


def update_user(uid, password, photoURL, username):
    try:
        user = auth.update_user(
            uid=uid,
            password=password,
            username=username,
            photoURL=photoURL
        )
    except Exception:
        return ErrorResponse(OperationNotFound(uid).message, 422, {'Content-Type': 'application/json'})

    if user is not None:
        update = User.getUser(user_id=user.uid)
        update.password = generate_password_hash(user.password)
        update.username = user.username
        update.photoURL = user.photoURL

        try:
            update.save_to_db()
        except Exception:
            return ErrorResponse(OperationNotFound(uid).message, 422, {'Content-Type': 'application/json'})

        return make_response(jsonify('Change Successful'), user.uid)

    else:
        return ErrorResponse(OperationNotFound(uid).message, 422, {'Content-Type': 'application/json'})
