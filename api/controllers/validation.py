import jwt
from flask import Blueprint, request, jsonify
from flask import current_app as app
from api.schemas.token import ValidTokenSchema
from api.schemas.operation import EmailVerificationOperation
from api.utils.encryptUtil import _decrypt, password
from api.utils.update_user import update_firebase_emailVerified
from api.models.user import User

router = Blueprint('Validator', __name__)


@router.route('/token')
def validate_reset_token():
    args = request.args
    if 'token' in args.keys():
        token = args.get('token')
    resp = {'id': token}
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
        resp['valid'] = True
        return jsonify(ValidTokenSchema().dump(resp).data)
    except Exception as e:
        resp['valid'] = False
        print(e)
        return jsonify(ValidTokenSchema().dump(resp).data)


@router.route('/email')
def validate_email():
    args = request.args
    if 'id' in args.keys():
        encryptID = args['id']
        email = _decrypt(encryptID, "", password)
        user = User.getUser(email=email)
        if not user:
            print('User not found')
        resp = {'id': user.id}
        if not update_firebase_emailVerified(user.id):
            print('Email not verified')
            resp['status'] = 'Not verified'
        else:
            resp['status'] = 'Verified'
        return jsonify(EmailVerificationOperation().dump(resp).data)
