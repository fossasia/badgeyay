import jwt
import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response
from api.models.user import User

router = Blueprint('resetUser', __name__)


@router.route('/password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

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
        return jsonify(
            Response(403).generateMessage(
                'No data received'))
