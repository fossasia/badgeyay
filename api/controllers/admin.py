from flask import jsonify, Blueprint
from api.models.user import User
from api.models.badges import Badges
from api.schemas.user import AllUsersSchema
from api.schemas.badges import AllBadges


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
