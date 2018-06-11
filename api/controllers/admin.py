from flask import jsonify, Blueprint, request
from api.db import db
from api.models.user import User
from api.models.badges import Badges
from api.models.file import File
from api.schemas.user import AllUsersSchema, UserAllowedUsage
from api.schemas.badges import AllBadges
from api.schemas.file import FileSchema
from api.schemas.errors import JsonNotFound
from api.utils.errors import ErrorResponse


router = Blueprint('admin', __name__)


@router.route('/show_all_users', methods=['GET'])
def show_all_users():
    users = User.query.all()
    schema = AllUsersSchema(many=True)
    result = schema.dump(users)
    return jsonify(result.data)


@router.route('/get_all_badges', methods=['GET'])
def get_all_badges():
    all_badges = Badges.query.all()
    schema = AllBadges(many=True)
    result = schema.dump(all_badges)
    return jsonify(result.data)


@router.route('/get_all_files', methods=['GET'])
def get_all_files():
    file = File().query.all()
    return jsonify(FileSchema(many=True).dump(file).data)


@router.route('/add_usage', methods=['POST'])
def admin_add_usage():
    try:
        data = request.get_json()['data']
        print(data)
    except Exception:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data['uid']
    allowed_usage = data['allowed_usage']
    user = User.getUser(user_id=uid)
    user.allowed_usage = user.allowed_usage + allowed_usage
    db.session.commit()

    return jsonify(UserAllowedUsage().dump(user).data)
