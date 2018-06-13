import jwt
from flask import Blueprint, request, jsonify
from flask import current_app as app
from api.schemas.token import ValidTokenSchema

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
