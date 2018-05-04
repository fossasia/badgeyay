from flask import Blueprint, jsonify, request
from utils.response import Response
from models.user import User

router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def registerUser():
    data = request.get_json()
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
