# from api.helpers.verifyToken import loginRequired
import os

from shutil import copyfile
from api.config import config

from flask import Blueprint, jsonify, request

from api.utils.errors import ErrorResponse
from api.models.badges import Badges
from api.models.user import User
from api.schemas.badges import BadgeSchema, UserBadges
from api.utils.merge_badges import MergeBadges
from api.utils.svg_to_png import SVG2PNG
from api.schemas.errors import (
    ImageNotFound,
    JsonNotFound,
    CSVNotFound
)


router = Blueprint('generateBadges', __name__)


@router.route('/generate_badges', methods=['POST'])
def generateBadges():
    try:
        data = request.get_json()['badge']
    except Exception:
        return ErrorResponse(JsonNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if not data['csv']:
        return ErrorResponse(CSVNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    if not data['image']:
        return ErrorResponse(ImageNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    csv_name = data.get('csv')
    image_name = data.get('image')
    text_color = data.get('font_color', '#ffffff')
    badge_size = data.get('badge_size', 'A3')
    font_size = data.get('font_size') or None
    font_choice = data.get('font_type') or None
    svg2png = SVG2PNG()
    if config.ENV == 'PROD':
        svg2png.do_text_fill(os.getcwd() + '/api/static/badges/8BadgesOnA3.svg', text_color)
    else:
        svg2png.do_text_fill('static/badges/8BadgesOnA3.svg', text_color)
    merge_badges = MergeBadges(image_name, csv_name, badge_size, font_size, font_choice)
    merge_badges.merge_pdfs()

    uid = data.get('uid')
    user_creator = User.getUser(user_id=uid)
    badge_created = Badges(image=image_name, csv=csv_name, text_color=text_color, badge_size='A3', creator=user_creator)
    badge_created.save_to_db()

    badgeFolder = badge_created.image.split('.')[0]
    badgePath = ''
    destFile = ''
    if config.ENV == 'LOCAL':
        badgePath = os.getcwd() + '/static/temporary/' + badgeFolder
        destFile = os.getcwd() + '/static/badges/' + badge_created.id + '.pdf'
    else:
        badgePath = os.getcwd() + '/api/static/temporary/' + badgeFolder
        destFile = os.getcwd() + '/api/static/badges/' + badge_created.id + '.pdf'
    if os.path.isdir(badgePath):
        print(badgePath)
        copyfile(badgePath + '/all-badges.pdf', destFile)

    return jsonify(BadgeSchema().dump(badge_created).data)


@router.route('/get_badges', methods=['GET'])
def get_badges():
    input_data = request.args
    user = User.getUser(user_id=input_data.get('uid'))
    badges = Badges().query.filter_by(creator=user)
    return jsonify(UserBadges(many=True).dump(badges).data)
