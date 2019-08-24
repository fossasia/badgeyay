import jwt
from flask import current_app as app
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from backend.models.user import User
from backend.schemas.errors import PayloadNotFound, SignatureExpired, PasswordNotFound
from backend.utils.errors import ErrorResponse
from backend.utils.update_user import update_firebase_password
from backend.schemas.operation import ResetPasswordOperation

router = Blueprint('Change Meta', __name__)


@router.route('/password', methods=['POST'])
def changePwd():
    try:
        data = request.get_json()['data']['attributes']
    except Exception as e:
        print(e)
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    token = data['token']
    try:
        decoded_res = jwt.decode(token, app.config['SECRET_KEY'])
    except Exception as e:
        print(e)
        return ErrorResponse(SignatureExpired().message, 422, {'Content-Type': 'application/json'}).respond()

    user = User.getUser(user_id=decoded_res['id'])

    if 'pwd' not in data.keys():
        return ErrorResponse(PasswordNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    pwd = data['pwd']
    oldPwd = user.password
    user.password = generate_password_hash(pwd)
    user.save_to_db()

    resp = {'id': token}
    if update_firebase_password(user.id, pwd):
        resp['status'] = 'Changed'
        return jsonify(ResetPasswordOperation().dump(resp).data)
    else:
        print('Firebase not uploaded')
        user.password = oldPwd
        user.save_to_db()
        resp['status'] = 'Not Changed'
        return jsonify(ResetPasswordOperation().dump(resp).data)
