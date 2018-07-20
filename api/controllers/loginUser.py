import jwt

from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.models.user import User
from api.models.permissions import Permissions
from api.schemas.user import FTLUserSchema
from api.schemas.token import LoginTokenSchema
from api.utils.errors import ErrorResponse
from api.schemas.errors import (
    UserNotFound,
    OperationNotFound,
)


router = Blueprint('loginUser', __name__)


@router.route('/login')
def login():
    args = request.args
    ip_addr = request.environ['REMOTE_ADDR']
    if 'id' in args.keys():
        user = User.getUser(user_id=args['id'])
        uid = user.id
        if not user:
            return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

        tokenObj = {'user': user.username}
        perm = Permissions.get_by_uid(user.id)
        if perm:
            if perm.isAdmin:
                tokenObj = {'adminStatus': True}
        # Token that is not expiring and validated for the whole session
        token = jwt.encode(
            tokenObj,
            app.config.get('SECRET_KEY'))

        # Saving the IP of the logged in user
        user.last_login_ip = ip_addr
        user.save_to_db()

        resp = {
            'id': user.id,
            'token': token.decode('UTF-8')}

        return jsonify(LoginTokenSchema().dump(resp).data)

    return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()


@router.route('/register/<uid>', methods=['GET'])
def index(uid):
    user = User.getUser(user_id=uid)
    schema = FTLUserSchema()
    return jsonify(schema.dump(user).data)
