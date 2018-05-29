from flask import Blueprint, jsonify, request
from api.utils.response import Response
from api.models.user import User
from api.helpers.verifyPassword import verifyPassword
from werkzeug.security import generate_password_hash

router = Blueprint('modifyUser', __name__)


@router.route('/password', methods=['PUT'])
def changePassword():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

    if data and data['username']:
        user = User.getUser(data['username'])
        if user:
            if not verifyPassword(user, data['password']):
                return jsonify(
                    Response(401).generateMessage(
                        'Wrong username and password combination'))
            user.password = generate_password_hash(data['newPassword'])
            try:
                user.save_to_db()
            except Exception as e:
                return jsonify(
                    Response(401).exceptWithMessage(
                        str(e),
                        'Unable to update password'))
            return jsonify(
                Response(200).generateMessage(
                    'Password Updated successfully'))
    else:
        return jsonify(Response(403).generateMessage('No data received'))


@router.route('/name', methods=['PUT'])
def changeName():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

    if data and data['username']:
        user = User.getUser(data['username'])
        if user:
            if not verifyPassword(user, data['password']):
                return jsonify(
                    Response(401).generateMessage(
                        'Wrong username and password combination'))
            user.name = data['name']
            try:
                user.save_to_db()
            except Exception as e:
                return jsonify(
                    Response(401).exceptWithMessage(
                        str(e),
                        'Unable to update name'))
            return jsonify(
                Response(200).generateMessage(
                    'Name Updated successfully'))
    else:
        return jsonify(
            Response(403).generateMessage(
                'No data received'))
