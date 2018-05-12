from flask import Blueprint, jsonify, request
from api.utils.response import Response
from api.models.user import User

router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def registerUser():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

    newUser = User(
        data['username'],
        data['password'],
        data['name'])

    try:
        newUser.save_to_db()
    except Exception as e:
        print(e)
        return jsonify(
            Response(401).generateMessage(
                'User already exists with the same Username'))

    return jsonify(
        Response(200).generateMessage(
            'User created successfully'))
