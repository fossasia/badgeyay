import uuid
from flask import jsonify, Blueprint, request
from api.models.user import User
from api.models.badges import Badges
from api.models.file import File
from api.models.admin import Admin
from api.schemas.user import AllUsersSchema
from api.schemas.badges import AllBadges
from api.schemas.file import FileSchema
from api.schemas.admin import AdminSchema


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
