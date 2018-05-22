import os
from flask import Blueprint, jsonify, request
from flask import current_app as app
# from api.helpers.verifyToken import loginRequired
from api.utils.response import Response
from api.utils.svg_to_png import SVG2PNG
from api.utils.merge_badges import MergeBadges
from api.models.user import User
from api.models.badges import Badges

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

    uid = data.get('uid')
    logo = data.get('event-logo')
    background_image = data.get('image')
    csv = data.get('csv')
    font = data.get('font')
    font_size = data.get('font-size')
    font_color = data.get('font-color') or '#ffffff'
    badge_size = data.get('badge-size') or 'A3'

    svg2png = SVG2PNG()
    svg2png.do_text_fill('static/badges/8BadgesOnA3.svg', font_color)
    merge_badges = MergeBadges(background_image, csv)
    merge_badges.merge_pdfs()

    user_creator = User.getUser(user_id=uid)
    generated_badge = Badges(event_logo=logo, background_image=background_image, csv=csv, font=font,
                             font_size=font_size, font_color=font_color, badge_size=badge_size, creator=user_creator)
    generated_badge.save_to_db()

    output = os.path.join(app.config.get('BASE_DIR'), 'static', 'temporary', background_image)

    return jsonify(
        Response(200).generateMessage(
            str(output)))
