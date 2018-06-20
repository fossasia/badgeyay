import os

from flask import Blueprint, request, jsonify
from api.utils.errors import ErrorResponse
from flask import current_app as app
from api.helpers.uploads import saveToImage
from api.helpers.verifyToken import loginRequired
from api.utils.firebaseUploader import fileUploader
from api.schemas.errors import (
    PayloadNotFound,
    ImageNotFound,
    UserNotFound,
    ExtensionNotFound
)
from api.schemas.user import UpdateUserSchema
from api.models.user import User

router = Blueprint('updateUserProfile', __name__)


@loginRequired
@router.route('/profileImage', methods=['POST'])
def update_profile_image():
    try:
        data = request.get_json()['data']['attributes']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if not data['image']:
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if not data['extension']:
        return ErrorResponse(ExtensionNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data['uid']
    image = data['image']
    extension = data['extension']

    try:
        imageName = saveToImage(imageFile=image, extension=extension)
    except Exception:
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    fetch_user, imageLink = update_database(uid, imageName)
    return jsonify(UpdateUserSchema().dump(fetch_user).data)


def update_database(uid, imageName):
    fetch_user = User.getUser(user_id=uid)
    if fetch_user is None:
        return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()
    imagePath = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'image') + '/' + imageName
    imageLink = fileUploader(imagePath, 'profile/images/' + imageName)
    fetch_user.photoURL = imageLink
    fetch_user.save_to_db()

    try:
        os.unlink(imagePath)
    except Exception:
        print('Unable to delete the temporary file')

    return fetch_user, imageLink
