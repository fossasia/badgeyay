from backend.db import db
from flask import request, Blueprint, jsonify
from backend.models.permissions import Permissions
from backend.schemas.errors import UserNotFound, FieldNotFound
from backend.utils.errors import ErrorResponse
from backend.schemas.permissions import ModifyPermissionsIncoming, ModifyPermissionsDone


router = Blueprint('changePermissions', __name__)


@router.route('/add/user', methods=['POST'])
def add_as_user():
    schema = ModifyPermissionsIncoming()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)

    if not data['isUser']:
        return ErrorResponse(FieldNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions = Permissions.get_by_uid(uid=data['uid'])

    if user_permissions is None:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions.isUser = True
    user_permissions.isAdmin = False
    user_permissions.isSales = False

    db.session.commit()

    return jsonify(ModifyPermissionsDone().dump(user_permissions).data)


@router.route('/add/sales', methods=['POST'])
def add_as_sales():
    schema = ModifyPermissionsIncoming()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)

    if not data['isSales']:
        return ErrorResponse(FieldNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions = Permissions.get_by_uid(uid=data['uid'])

    if user_permissions is None:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions.isUser = False
    user_permissions.isAdmin = False
    user_permissions.isSales = True

    db.session.commit()

    return jsonify(ModifyPermissionsDone().dump(user_permissions).data)


@router.route('/add/admin', methods=['POST'])
def add_as_admin():
    schema = ModifyPermissionsIncoming()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)

    if not data['isAdmin']:
        return ErrorResponse(FieldNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions = Permissions.get_by_uid(uid=data['uid'])

    if user_permissions is None:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    user_permissions.isUser = False
    user_permissions.isAdmin = True
    user_permissions.isSales = False

    db.session.commit()

    return jsonify(ModifyPermissionsDone().dump(user_permissions).data)
