import base64
import os
from api.utils.svg_to_png import SVG2PNG
from flask import Blueprint, request, jsonify
from api.utils.errors import ErrorResponse
from api.helpers.verifyToken import loginRequired
from api.helpers.uploads import saveToImage, saveToCSV, saveAsCSV
from api.models.file import File
from api.models.user import User
from api.schemas.file import (
    FileSchema,
    ManualFileSchema,
    CSVUploadSchema,
    ImageFileSchema,
    DefImageSchem,
    ColorImageSchema
)
from flask import current_app as app
from api.schemas.errors import (
    UserNotFound,
    ImageNotFound,
    PayloadNotFound,
    OperationNotFound,
    ManualDataNotFound,
    ExtensionNotFound,
    CSVNotFound
)


router = Blueprint('fileUploader', __name__)


@router.route('/image', methods=['POST'])
@loginRequired
def uploadImage():
    try:
        data = request.get_json()['imgFile']
        image = data['imgFile']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    extension = data['extension']
    try:
        imageName = saveToImage(imageFile=image, extension=extension)
    except Exception:
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data['uid']
    fetch_user = User.getUser(user_id=uid)
    if fetch_user is None:
        return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

    file_upload = File(filename=imageName, filetype='image', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(ImageFileSchema().dump(file_upload).data)


@router.route('/file', methods=['POST'])
@loginRequired
def fileUpload():
    try:
        data = request.json['csvFile']
        csv = data['csvFile']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if 'extension' not in data.keys():
        return ErrorResponse(ExtensionNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    extension = data['extension']
    if extension != 'csv':
        return ErrorResponse(CSVNotFound().message, 422, {'Content-Type': 'application/json'}).respond()
    try:
        csvName = saveToCSV(csvFile=csv, extension='.csv')
    except Exception:
        return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data.get('uid')
    fetch_user = User.getUser(user_id=uid)
    if fetch_user is None:
        return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

    file_upload = File(filename=csvName, filetype='csv', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(CSVUploadSchema().dump(file_upload).data)


@router.route('/manual_data', methods=['POST'])
@loginRequired
def upload_manual_data():
    try:
        data = request.get_json()['data']['attributes']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if not data.get('manual_data'):
        return ErrorResponse(ManualDataNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data.get('uid')
    manual_data = data.get('manual_data')
    fetch_user = User.getUser(user_id=uid)
    if fetch_user is None:
        return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

    try:
        csvName = saveAsCSV(csvData=manual_data)
    except Exception:
        return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    file_upload = File(filename=csvName, filetype='csv', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(ManualFileSchema().dump(file_upload).data)


@router.route('/get_file', methods=['GET'])
@loginRequired
def get_file():
    input_data = request.args
    file = File().query.filter_by(filename=input_data.get('filename')).first()
    return jsonify(FileSchema().dump(file).data)


@router.route('/upload_default', methods=['POST'])
@loginRequired
def upload_default():
    try:
        data = request.get_json()['data']['attributes']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data.get('uid')
    image_name = data.get('defaultImage') + ".png"
    image_data = None
    with open(os.path.join(app.config.get('BASE_DIR'), 'badge_backgrounds', image_name), "rb") as image_file:
        image_data = base64.b64encode(image_file.read())

    try:
        imageName = saveToImage(imageFile=image_data.decode('utf-8'), extension=".png")
    except Exception as e:
        print(e)
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    fetch_user = User.getUser(user_id=uid)
    file_upload = File(filename=imageName, filetype='image', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(DefImageSchem().dump(file_upload).data)


@router.route('/background_color', methods=['POST'])
@loginRequired
def background_color():
    try:
        data = request.get_json()['data']['attributes']
        bg_color = data['bg_color']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    svg2png = SVG2PNG()

    bg_color = '#' + str(bg_color)
    user_defined_path = svg2png.do_svg2png(1, bg_color)
    with open(user_defined_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read())
        os.remove(user_defined_path)

    try:
        imageName = saveToImage(imageFile=image_data.decode('utf-8'), extension=".png")
    except Exception:
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    uid = data['uid']
    fetch_user = User.getUser(user_id=uid)
    if fetch_user is None:
        return ErrorResponse(UserNotFound(uid).message, 422, {'Content-Type': 'application/json'}).respond()

    file_upload = File(filename=imageName, filetype='image', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(ColorImageSchema().dump(file_upload).data)
