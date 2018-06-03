# from api.helpers.verifyToken import loginRequired
import os

from shutil import copyfile
from api.config import config

from flask import Blueprint, jsonify, request

from api.models.badges import Badges
from api.models.user import User
from api.schemas.badges import BadgeSchema
from api.utils.merge_badges import MergeBadges
from api.utils.response import Response
from api.utils.svg_to_png import SVG2PNG

router = Blueprint('generateBadges', __name__)


@router.route('/generate_badges', methods=['POST'])
def generateBadges():
    try:
        data = request.get_json()['badge']
    except Exception as e:
        return jsonify(
            Response(401).exceptWithMessage(
                str(e),
                'Could not find any JSON'))

    if not data['csv']:
        return jsonify(
            Response(401).generateMessage(
                'No CSV filename found'))
    if not data['image']:
        return jsonify(
            Response(401).generateMessage(
                'No Image filename found'))

    csv_name = data.get('csv')
    image_name = data.get('image')
    text_color = data.get('font_color', '#ffffff')
    badge_size = data.get('badge_size', 'A3')
    svg2png = SVG2PNG()
    svg2png.do_text_fill('static/badges/8BadgesOnA3.svg', text_color)
    merge_badges = MergeBadges(image_name, csv_name, badge_size)
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
