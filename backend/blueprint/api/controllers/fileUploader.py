from flask import Blueprint, request, jsonify
from utils.response import Response
from helpers.verifyToken import loginRequired
from helpers.uploads import saveToImage


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
