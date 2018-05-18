from flask import Blueprint, jsonify, request
from firebase_admin import auth
from api.utils.response import Response
from api.models.user import User

router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def registerUser():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(500).exceptWithMessage(
                str(e),
                'Unable to get json'))

    user = auth.create_user(
        email=data['email'],
        email_verified=False,
        password=data['example'],
        display_name=data['name'],
    )

    newUser = User(
        id_=user.uid,
        username=user.display_name,
        email=user.email,
        password=data['password'])

    try:
        newUser.save_to_db()
    except Exception as e:
        return jsonify(
            Response(401).exceptWithMessage(
                str(e),
                'User already exists with the same Username'))

    return jsonify(
        Response(200).generateMessage(
            'User created successfully'))
