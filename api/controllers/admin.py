import uuid
from flask import jsonify, Blueprint, request
from api.db import db
from api.models.user import User
from api.models.badges import Badges
from api.models.file import File
from api.models.admin import Admin
from api.schemas.user import AllUsersSchema, UserAllowedUsage
from api.schemas.badges import AllBadges, DatedBadgeSchema
from api.schemas.file import FileSchema
from api.schemas.errors import JsonNotFound
from api.schemas.admin import AdminSchema
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


@router.route('/register_admin', methods=['POST'])
def register_admin():
    schema = AdminSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    admin = Admin(
        id_=str(uuid.uuid4()),
        username=data['username'],
        password=data['password'],
        email=data['email'])
    try:
        admin.save_to_db()
    except Exception as e:
        return jsonify(e)

    return jsonify(schema.dump(admin).data)


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


@router.route('/get_badges_dated', methods=['POST'])
def get_badges_dated():
    schema = DatedBadgeSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    dated_badges = Badges.query.filter(Badges.created_at <= data.get('end_date')).filter(Badges.created_at >= data.get('start_date'))
    return jsonify(AllBadges(many=True).dump(dated_badges).data)
