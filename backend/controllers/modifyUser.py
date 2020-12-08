from flask import Blueprint, jsonify, request
from backend.db import db
from backend.utils.response import Response
from backend.utils.update_user import update_firebase_complete
from backend.models.user import User
from backend.helpers.verifyToken import loginRequired
from backend.utils.errors import ErrorResponse
from backend.helpers.verifyPassword import verifyPassword
from werkzeug.security import generate_password_hash
from backend.schemas.user import DeleteUserSchema, UpdateProfileSchema, UserSchema
from backend.schemas.errors import (
    PayloadNotFound,
    OperationNotFound,
    PasswordNotFound,
    JsonNotFound
)

router = Blueprint('modifyUser', __name__)

@router.route('/password', methods=['PUT'])
@loginRequired
def changePassword():
    try:
        data = request.get_json()
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if data and data['username']:
        user = User.getUser(username=data['username'])
        if user:
            if not verifyPassword(user, data['password']):
                return ErrorResponse(PasswordNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

            user.password = generate_password_hash(data['newPassword'])
            try:
                user.save_to_db()
            except Exception:
                return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

            return jsonify(
                Response(200).generateMessage(
                    'Password Updated successfully'))
    else:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

@router.route('/name', methods=['PUT'])
@loginRequired
def changeName():
    try:
        data = request.get_json()
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if data and data['username']:
        user = User.getUser(username=data['username'])
        if user:
            if not verifyPassword(user, data['password']):
                return ErrorResponse(PasswordNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

            user.name = data['name']
            try:
                user.save_to_db()
            except Exception:
                return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

            return jsonify(
                Response(200).generateMessage(
                    'Name Updated successfully'))
    else:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

@router.route('/delete', methods=['DELETE'])
@loginRequired
def delete_user():
    schema = DeleteUserSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    user = User.getUser(user_id=data['uid'])
    temp_user = user
    user.delete_user()
    return jsonify(DeleteUserSchema().dump(temp_user).data)

@router.route('/update_profile', methods=['POST'])
@loginRequired
def update_profile():
    schema = UpdateProfileSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    user = User.getUser(user_id=data['uid'])
    if data['email'] != '':
        user.email = data['email']
    if data['password'] != '':
        user.password = data['password']
    if data['username'] != '':
        user.username = data['username']

    db.session.commit()

    ret = update_firebase_complete(data['uid'], data['username'], data['email'], data['password'])
    print(ret)
    return jsonify(UserSchema().dump(user).data)
