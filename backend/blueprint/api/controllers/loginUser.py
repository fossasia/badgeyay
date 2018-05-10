import jwt
import datetime

from flask import Blueprint, jsonify, request
from flask import current_app as app
from utils.response import Response
from helpers.verifyPassword import verifyPassword
from models.user import User


router = Blueprint('loginUser', __name__)


@router.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

    if data and data['username']:
        user = User.query.filter_by(username=data['username']).first()
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
            app.config['SECRET_KEY'])

        return jsonify(
            Response(200).generateToken(
                token.decode('UTF-8')))

    return jsonify(
        Response(403).generateMessage(
            'No data received'))
