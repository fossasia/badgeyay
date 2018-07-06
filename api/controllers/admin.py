from flask import jsonify, Blueprint, request
from api.db import db
from api.models.user import User
from api.models.socialContent import SocialContent
from api.models.badges import Badges
from api.models.file import File
from api.models.utils import Utilities
from api.models.modules import Module
from api.schemas.modules import ModuleSchema
from api.helpers.verifyToken import adminRequired
from api.schemas.user import AllUsersSchema, UserAllowedUsage, DatedUserSchema
from api.schemas.badges import DatedBadgeSchema
from api.schemas.badges import AllBadges, AllGenBadges
from api.schemas.file import FileSchema
from api.schemas.errors import JsonNotFound
from api.schemas.admin import (
    AdminSchema,
    AllUserStat,
    AdminMailStat,
    AllAdminRole,
    DeleteAdminRole,
    SocialMedia,
    AdminBadgeSchema,
    AdminReportSchema
)
from api.schemas.utils import SetPricingSchema, ReturnSetPricing
from api.utils.errors import ErrorResponse
from api.schemas.errors import UserNotFound
from api.helpers.verifyToken import loginRequired
from flask import current_app as app
from firebase_admin import db as firebasedb
from dateutil.relativedelta import relativedelta
import datetime


router = Blueprint('admin', __name__)


@router.route('/show_all_users', methods=['GET'])
@adminRequired
def show_all_users():
    page = request.args.get('page', 1, type=int)
    args = request.args
    if 'email' in args.keys():
        user = User.getUser(email=args['email'])
        if not user:
            return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
        return jsonify(AllUsersSchema().dump(user).data)
    schema = AllUsersSchema(many=True)
    if 'state' in args.keys():
        if args['state'] == 'deleted':
            users = User.query.filter(User.deleted_at.isnot(None)).paginate(
                page, app.config['POSTS_PER_PAGE'], False)
        if args['state'] == 'active':
            users = User.query.filter(User.deleted_at.is_(None)).paginate(
                page, app.config['POSTS_PER_PAGE'], False)
        if args['state'] == 'all':
            users = User.query.paginate(
                page, app.config['POSTS_PER_PAGE'], False)
    result = schema.dump(users.items)
    return jsonify(result.data)


@router.route('/all-modules', methods=['GET'])
@adminRequired
def get_all_modules():
    module = Module.query.all()[0]
    return jsonify(ModuleSchema().dump(module).data)


@router.route('/all-badge-detail', methods=['GET'])
@adminRequired
def get_all_badge_detail():
    args = request.args
    page = request.args.get('page', 1, type=int)
    if 'state' in args.keys():
        schema = AdminBadgeSchema(many=True)
        if args['state'] == 'all':
            badges = Badges.query.paginate(
                page, app.config['POSTS_PER_PAGE'], False)
        if args['state'] == 'created':
            badges = Badges.query.paginate(
                page, app.config['POSTS_PER_PAGE'], False)
        if args['state'] == 'deleted':
            badges = Badges.query.paginate(
                page, app.config['POSTS_PER_PAGE'], False)
        return jsonify(schema.dump(badges.items).data)


@router.route('/admin-report', methods=['GET'])
@adminRequired
def get_admin_report():
    page = request.args.get('page', 1, type=int)

    curr_date = datetime.datetime.utcnow() - relativedelta(days=app.config["POSTS_PER_PAGE"] * (page - 1))
    payload = []
    schema = AdminReportSchema(many=True)
    for i in range(1, app.config['POSTS_PER_PAGE']):
        date_start = curr_date - relativedelta(days=i)
        date_end = curr_date - relativedelta(days=i - 1)
        badge_count = Badges.query.filter(
            Badges.created_at.between(date_start, date_end)).count()
        user_creation_count = User.query.filter(
            User.created_at.between(date_start, date_end)).count()
        user_deletion_count = User.query.filter(
            User.deleted_at.between(date_start, date_end)).count()
        report = {
            'id': date_start,
            'badgeCount': badge_count,
            'userCreationCount': user_creation_count,
            'userDeletionCount': user_deletion_count}
        payload.append(report)
    return jsonify(schema.dump(payload).data)


@router.route('/all-modules/<id_>', methods=['PATCH'])
@adminRequired
def patch_module(id_):
    module = Module.query.filter_by(id=id_).first()
    data = request.get_json()['data']['attributes']
    module.ticketInclude = data['ticketInclude']
    module.paymentInclude = data['ticketInclude']
    module.donationInclude = data['donationInclude']
    module.save_to_db()
    return jsonify(ModuleSchema().dump(module).data)


@router.route('/show_all_users/<userid>', methods=['PATCH'])
@adminRequired
def update_user(userid):
    user = User.getUser(user_id=userid)
    if not user:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
    data = request.get_json()['data']['attributes']
    if not data:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
    for key in data:
        setattr(user, key, data[key])
    user.save_to_db()
    schema = AllUsersSchema()
    result = schema.dump(user)
    return jsonify(result.data)


@router.route('/show_all_users/<userid>', methods=['DELETE'])
@adminRequired
def delete_user(userid):
    user = User.getUser(user_id=userid)
    if not user:
        return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
    user.deleted_at = datetime.datetime.utcnow()
    user.save_to_db()
    schema = AllUsersSchema()
    result = schema.dump(user)
    return jsonify(result.data)


@router.route('/admin-stat-mail', methods=['GET'])
def get_admin_stat():
    mail_ref = firebasedb.reference('mails')
    mail_resp = mail_ref.get()
    mail_list = []
    for key in mail_resp:
        mail_list.append(mail_resp[key])
    mail_list.sort(key=lambda e: e['date'], reverse=True)
    for item in mail_list:
        item['date'] = datetime.datetime.strptime(
            item['date'], '%Y-%m-%dT%H:%M:%SZ')
    curr_date = datetime.datetime.utcnow()
    prev_month_date = curr_date - relativedelta(months=1)
    last_three_days_date = curr_date - relativedelta(days=3)
    last_seven_days_date = curr_date - relativedelta(days=7)
    last_day_date = curr_date - relativedelta(days=1)

    prev_month_cnt = len(
        [mail for mail in mail_list if mail['date'] >= prev_month_date])
    last_three_days_cnt = len(
        [mail for mail in mail_list if mail['date'] >= last_three_days_date])
    last_day_cnt = len(
        [mail for mail in mail_list if mail['date'] >= last_day_date])
    last_seven_days_cnt = len(
        [mail for mail in mail_list if mail['date'] >= last_seven_days_date])

    payload = {
        'id': datetime.datetime.utcnow(),
        'lastDayCount': last_day_cnt,
        'lastThreeDays': last_three_days_cnt,
        'lastMonth': prev_month_cnt,
        'lastSevenDays': last_seven_days_cnt}

    return jsonify(AdminMailStat().dump(payload).data)


@router.route('/all-badge', methods=['GET'])
@adminRequired
def all_generated_badges():
    badge_cnt = len(Badges.query.all())
    dataPayload = {
        'id': datetime.datetime.now(),
        'cnt': str(badge_cnt)}
    return jsonify(AllGenBadges().dump(dataPayload).data)


@router.route('/all-admin', methods=['GET'])
def get_all_admin():
    admin_users = User.query.filter_by(siteAdmin=True).all()
    return jsonify(AllAdminRole(many=True).dump(admin_users).data)


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
    all_badges = Badges.query.paginate(
        page, app.config['POSTS_PER_PAGE'], False).items
    schema = AllBadges(many=True)
    result = schema.dump(all_badges)
    return jsonify(result.data)


@router.route('/get_all_files', methods=['GET'])
@loginRequired
def get_all_files():
    page = request.args.get('page', 1, type=int)
    files = File.query.paginate(
        page, app.config['POSTS_PER_PAGE'], False).items
    return jsonify(FileSchema(many=True).dump(files).data)


@router.route('/register_admin', methods=['POST'])
@adminRequired
def register_admin():
    schema = AdminSchema()
    input_data = request.get_json()['data']['attributes']
    if 'email' in input_data.keys():
        user = User.getUser(email=input_data['email'])
        if 'adminStat' in input_data.keys():
            user.siteAdmin = input_data['adminStat']
        user.save_to_db()
        return jsonify(schema.dump(user).data)
    else:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()


@router.route('/delete-admin', methods=['GET'])
@adminRequired
def delete_admin():
    args = request.args
    if 'email' in args.keys():
        user = User.getUser(email=args['email'])
        if not user:
            return ErrorResponse(UserNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
        user.siteAdmin = False
        user.save_to_db()
        return jsonify(DeleteAdminRole().dump(user).data)


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
    dated_badges = Badges.query.filter(Badges.created_at <= data.get(
        'end_date')).filter(Badges.created_at >= data.get('start_date'))
    return jsonify(AllBadges(many=True).dump(dated_badges).data)


@router.route('/get_users_dated', methods=['POST'])
def get_user_dated():
    schema = DatedUserSchema()
    input_data = request.get_json()
    data, err = schema.load(input_data)
    if err:
        return jsonify(err)
    dated_users = User.query.filter(User.created_at <= data.get(
        'end_date')).filter(User.created_at >= data.get('start_date'))
    return jsonify(AllUsersSchema(many=True).dump(dated_users).data)


@router.route('/set_pricing', methods=['POST'])
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


@router.route('/get_pricing', methods=['GET'])
def get_pricing():
    utils = Utilities.query.first()
    ret_data = {
        'status': 200,
        'pricing': utils.pricing,
        'message': 'Pricing Information'
    }
    return jsonify(ReturnSetPricing().dump(ret_data).data)


@router.route('/social-media', methods=['GET'])
def get_all_social_media():
    social_media = SocialContent.query.all()
    return jsonify(SocialMedia(many=True).dump(social_media).data)


@router.route('/social-media/<media>', methods=['PATCH'])
@adminRequired
def patch_social_media(media):
    social_media = SocialContent.check_key(media)
    if social_media:
        data = request.get_json()['data']['attributes']
        social_media.link = data['link']
        social_media.save_to_db()
        return jsonify(SocialMedia().dump(social_media).data)
