from flask import Blueprint, jsonify, request
from api.utils.response import Response
from firebase_admin import auth

router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def registerUser():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).generateMessage(
                str(e)))

    try:
        auth.create_user(
            display_name=data['name'],
            email=data['email'],
            phone_number=data['phone_number'],
            photo_url=data['photo_url'],
            password=data['password']
        )
    except Exception as e:
        auth.AuthError(500, e)

    return jsonify(Response(200).generateMessage('Sucessfully created new user'))
