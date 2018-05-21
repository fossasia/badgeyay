import os
from flask import Blueprint, jsonify, request
from flask import current_app as app
# from api.helpers.verifyToken import loginRequired
from api.utils.response import Response
from api.utils.svg_to_png import SVG2PNG
from api.utils.merge_badges import MergeBadges
from api.models.badges import Badges
from api.models.user import User

router = Blueprint('generateBadges', __name__)


@router.route('/generate_badges', methods=['POST'])
def generateBadges():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(
            Response(401).exceptWithMessage(
                str(e),
                'Could not find any JSON'))

    if not data.get('csv'):
        return jsonify(
            Response(401).generateMessage(
                'No CSV filename found'))
    if not data.get('image'):
        return jsonify(
            Response(401).generateMessage(
                'No Image filename found'))
    csv_name = data.get('csv')
    image_name = data.get('image')
    text_color = data.get('text-color') or '#ffffff'
    svg2png = SVG2PNG()
    svg2png.do_text_fill('static/badges/8BadgesOnA3.svg', text_color)
    merge_badges = MergeBadges(image_name, csv_name)
    merge_badges.merge_pdfs()

    uid = data.get('uid')
    user_creator = User.getUser(user_id=uid)
    badge_created = Badges(image=image_name, csv=csv_name, text_color=text_color, badge_size='A3', creator=user_creator)
    badge_created.save_to_db()

    output = os.path.join(app.config.get('BASE_DIR'), 'static', 'temporary', image_name)

    return jsonify(
        Response(200).generateMessage(
            str(output)))
