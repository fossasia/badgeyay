import os
import base64
from api.utils.response import Response
from flask import Blueprint, jsonify

router = Blueprint('assethelper', __name__)


@router.route('/default_images', methods=['GET'])
def getDefaultBackgrounds():
    bgDir = os.path.abspath(os.path.join(os.getcwd(), 'badge_backgrounds/'))
    resp = []
    for root, dir_, files in os.walk(os.path.normpath(bgDir)):
        for idx, file_ in enumerate(files):
            if file_ == 'user_defined.png':
                continue
            encode_string = ''
            with open(bgDir + '/' + file_, 'rb') as image_file:
                encode_string = base64.b64encode(image_file.read())
            obj = {}
            obj['id'] = idx
            obj['type'] = 'def-image'
            obj['attributes'] = {
                'name': file_,
                'imgData': encode_string.decode('utf-8')
            }
            resp.append(obj)
    resp_ = {'data': resp}
    return jsonify(Response(200).generateMessage(resp_, 'Image Response'))
