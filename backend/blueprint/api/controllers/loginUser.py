import jwt
import datetime

from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response
from api.helpers.verifyPassword import verifyPassword
from api.models.user import User


router = Blueprint('loginUser', __name__)


@router.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).exceptWithMessage(
                str(e),
                'Unable to get json'))

    if 'name' in data.keys():
        user = User.getUser(username=data['name'])
        if not user:
            return jsonify(
                Response(403).generateMessage(
                    'Could not find the Username Specified'))

        if not verifyPassword(user, data['password']):
            return jsonify(
                Response(401).generateMessage(
                    'Wrong username & password combination'))

        token = jwt.encode(
            {'user': user.username,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
            app.config.get('SECRET_KEY'))

        return jsonify(
            Response(200).generateToken(
                token.decode('UTF-8')))

    return jsonify(
        Response(403).generateMessage(
            'No name key received'))
