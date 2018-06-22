import os

from api.config import config
from flask import Blueprint, jsonify
from api.helpers.verifyToken import loginRequired

router = Blueprint('assethelper', __name__)


@loginRequired
@router.route('/default_images', methods=['GET'])
def getDefaultBackgrounds():
    if config.ENV == 'LOCAL':
        bgDir = os.path.abspath(os.path.join(os.getcwd(), 'badge_backgrounds/'))
    else:
        bgDir = os.path.abspath(os.path.join(os.getcwd(), 'api/badge_backgrounds/'))
    resp = []
    for root, dir_, files in os.walk(os.path.normpath(bgDir)):
        for idx, file_ in enumerate(files):
            if file_ == 'user_defined.png':
                continue
            obj = {}
            obj['id'] = idx
            obj['type'] = 'def-image'
            obj['attributes'] = {
                'name': file_.split('.')[0],
            }
            resp.append(obj)
    resp_ = {'data': resp}
    return jsonify(resp_)
