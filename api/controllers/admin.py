import uuid
from flask import jsonify, Blueprint, request
from api.db import db
from api.models.user import User
from api.models.badges import Badges
from api.models.file import File
from api.models.admin import Admin
from api.models.utils import Utilities
from api.helpers.verifyToken import adminRequired
from api.schemas.user import AllUsersSchema, UserAllowedUsage, DatedUserSchema
from api.schemas.badges import DatedBadgeSchema
from api.schemas.badges import AllBadges, AllGenBadges
from api.schemas.file import FileSchema
from api.schemas.errors import JsonNotFound
from api.schemas.admin import AdminSchema, AllUserStat
from api.schemas.utils import SetPricingSchema, ReturnSetPricing
from api.utils.errors import ErrorResponse
from api.helpers.verifyToken import loginRequired
from flask import current_app as app
import datetime


router = Blueprint('admin', __name__)


@router.route('/show_all_users', methods=['GET'])
def show_all_users():
    page = request.args.get('page', 1, type=int)
    schema = AllUsersSchema(many=True)
    users = User.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
    result = schema.dump(users.items)
    return jsonify(result.data)


@router.route('/all-badge', methods=['GET'])
@adminRequired
def all_generated_badges():
    badge_cnt = len(Badges.query.all())
    dataPayload = {
        'id': datetime.datetime.now(),
        'cnt': str(badge_cnt)}
    return jsonify(AllGenBadges().dump(dataPayload).data)


@router.route('/all-user', methods=['GET'])
@adminRequired
def all_users_stat():
    admin_cnt = len(User.query.filter_by(siteAdmin=True).all())
    reg_users = len(User.query.all()) - admin_cnt
    payload = {
        'id': datetime.datetime.now(),
        'superAdmin': str(admin_cnt),
        'registered': str(reg_users)}
    return jsonify(AllUserStat().dump(payload).data)


@router.route('/get_all_badges', methods=['GET'])
@loginRequired
def get_all_badges():
    page = request.args.get('page', 1, type=int)
    all_badges = Badges.query.paginate(page, app.config['POSTS_PER_PAGE'], False).items
    schema = AllBadges(many=True)
    result = schema.dump(all_badges)
    return jsonify(result.data)


@router.route('/get_all_files', methods=['GET'])
@loginRequired
def get_all_files():
    page = request.args.get('page', 1, type=int)
    files = File.query.paginate(page, app.config['POSTS_PER_PAGE'], False).items
    return jsonify(FileSchema(many=True).dump(files).data)


@router.route('/register_admin', methods=['POST'])
@loginRequired
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
@loginRequired
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


@router.route('/get_users_dated', methods=['POST'])
def get_user_dated():
    schema = DatedUserSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    dated_users = User.query.filter(User.created_at <= data.get('end_date')).filter(User.created_at >= data.get('start_date'))
    return jsonify(AllUsersSchema(many=True).dump(dated_users).data)


@router.route('/pricing', methods=['POST'])
def set_pricing():
    schema = SetPricingSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    utils = Utilities(pricing=data['pricing'])
    Utilities.query.delete()
    utils.save_to_db()
    ret_data = {
        'status': 200,
        'pricing': data['pricing'],
        'message': 'Pricing Set Successfully'
    }
    return jsonify(ReturnSetPricing().dump(ret_data).data)
