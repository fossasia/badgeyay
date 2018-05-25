from flask import Blueprint, request, jsonify
from api.utils.response import Response
from api.helpers.verifyToken import loginRequired
from api.helpers.uploads import saveToImage, saveToCSV, saveAsCSV
from api.models.file import File
from api.models.user import User


router = Blueprint('fileUploader', __name__)


@router.route('/image', methods=['POST'])
def uploadImage():
    try:
        data = request.json['imgFile']
        image = data['imgFile']
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'No Image is specified'))

    extension = data['extension']
    try:
        imageName = saveToImage(imageFile=image, extension=extension)
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'Image could not be uploaded'))

    uid = data['uid']
    fetch_user = User.getUser(user_id=uid)
    file_upload = File(filename=imageName, filetype='image', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(
        Response(200).generateMessage({
            'message': 'Image Uploaded Successfully',
            'unique_id': imageName}, 'image response'))


@router.route('/file', methods=['POST'])
def fileUpload():
    try:
        data = request.json['csvFile']
        csv = data['csvFile']
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'No CSV Specified'))
    if 'extension' not in data.keys():
        return jsonify(
            Response(403).generateErrorMessage(
                'No extension key received', 'error'))
    extension = data['extension']
    if extension != 'csv':
        return jsonify(Response(400).generateErrorMessage(
            'Bad extension! csv not found', 'error'))
    try:
        csvName = saveToCSV(csvFile=csv, extension='.csv')
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'CSV File could not be uploaded'))

    uid = data.get('uid')
    fetch_user = User.getUser(user_id=uid)
    file_upload = File(filename=csvName, filetype='csv', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(
        Response(200).generateMessage({
            'message': 'CSV Uploaded successfully',
            'unique_id': csvName}, 'csv response'))


@router.route('/manual_data', methods=['POST'])
@loginRequired
def upload_manual_data():
    try:
        data = request.get_json()
    except Exception as e:
        return(jsonify(
            Response(401).exceptWithMessage(
                str(e),
                'No data was provided')))

    if not data.get('manual_data'):
        return(jsonify(
            Response(400).generateErrorMessage(
                'No Manual Data is specified', 'error')))

    uid = data.get('uid')
    manual_data = data.get('manual_data')
    fetch_user = User.getUser(user_id=uid)
    try:
        csvName = saveAsCSV(csvData=manual_data)
    except Exception as e:
        return(jsonify(
            Response(401).exceptWithMessage(
                str(e),
                'Manual Data could not be uploaded')))

    file_upload = File(filename=csvName, filetype='csv', uploader=fetch_user)
    file_upload.save_to_db()
    return jsonify(
        Response(200).generateMessage({
            'message': 'Manual Data uploaded successfully',
            'unique_id': csvName}, 'csv response'))
