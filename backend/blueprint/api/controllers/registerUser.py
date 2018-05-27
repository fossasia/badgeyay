from flask import Blueprint, jsonify, request
from firebase_admin import auth
from api.models.user import User
from api.schemas.user import UserSchema


router = Blueprint('registerUser', __name__)


@router.route('/register', methods=['POST'])
def register_user():
    schema = UserSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return err
    user = auth.create_user(
        email=data['email'],
        email_verified=False,
        password=data['password'],
        display_name=data['name'],
    )

    newUser = User(
        id_=user.uid,
        username=data['name'],
        email=user.email,
        password=data['password'])

    newUser.save_to_db()

    return jsonify(schema.dump(newUser))
