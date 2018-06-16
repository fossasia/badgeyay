import jwt
from flask import current_app as app
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from api.models.user import User
from api.schemas.errors import PayloadNotFound, SignatureExpired, PasswordNotFound
from api.utils.errors import ErrorResponse
from api.schemas.user import UpdateUserSchema
from api.utils.update_user import update_firebase_password

router = Blueprint('Change Meta', __name__)


@router.route('/password', methods=['POST'])
def changePwd():
    try:
        data = request.get_json()['data']['attributes']
    except Exception as e:
        print(e)
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'})

    token = data['token']
    try:
        decoded_res = jwt.decode(token, app.config['SECRET_KEY'])
    except Exception as e:
        print(e)
        return ErrorResponse(SignatureExpired().message, 422, {'Content-Type': 'application/json'})

    user_email = decoded_res['email']
    user = User.getUser(username=user_email)

    if 'pwd' not in data.keys():
        return ErrorResponse(PasswordNotFound().message, 422, {'Content-Type': 'application/json'})

    pwd = data['pwd']
    oldPwd = user.password
    user.password = generate_password_hash(pwd)
    user.save_to_db()

    if update_firebase_password(user.uid, pwd):
        return jsonify(UpdateUserSchema().dump(user).data)
    else:
        print('Firebase not uploaded')
        user.password = oldPwd
        user.save_to_db()
        return jsonify(UpdateUserSchema().dump(user).data)
