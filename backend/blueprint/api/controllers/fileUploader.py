from flask import Blueprint, request, jsonify
from utils.response import Response
from helpers.verifyToken import loginRequired
from helpers.uploads import saveToImage, saveToCSV


router = Blueprint('fileUploader', __name__)


@router.route('/image', methods=['POST'])
@loginRequired
def uploadImage():
    try:
        image = request.json['data']
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'No Image is specified'))

    extension = request.json['extension']
    try:
        imageName = saveToImage(imageFile=image, extension=extension)
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'Image could not be uploaded'))

    return jsonify(
        Response(200).generateMessage({
            'message': 'Image Uploaded Successfully',
            'unique_id': imageName}))


@router.route('/file', methods=['POST'])
@loginRequired
def fileUpload():
    if 'file' not in request.files:
        return jsonify(
            Response(401).generateMessage(
                'No file is specified'))

    file = request.files['file']
    try:
        csvName = saveToCSV(csvFile=file, extension='.csv')
    except Exception as e:
        return jsonify(
            Response(400).exceptWithMessage(
                str(e),
                'CSV File could not be uploaded'))

    return jsonify(
        Response(200).generateMessage({
            'message': 'CSV Uploaded successfully',
            'unique_id': csvName}))
