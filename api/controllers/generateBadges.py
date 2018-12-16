import os
import datetime

from shutil import rmtree
from api.config import config
from flask import current_app as app

from flask import Blueprint, jsonify, request

from api.db import db
from api.helpers.verifyToken import loginRequired
from api.utils.errors import ErrorResponse
from api.models.badges import Badges
from api.models.user import User
from api.schemas.badges import BadgeSchema, UserBadges, DeletedBadges
from api.utils.merge_badges import MergeBadges
from api.utils.svg_to_png import SVG2PNG
from api.schemas.errors import (
    ImageNotFound,
    JsonNotFound,
    CSVNotFound,
    UsageNotAllowed
)
from firebase_admin import db as firebase_db
from api.utils.firebaseUploader import fileUploader, deleteFile


router = Blueprint('generateBadges', __name__)


@router.route('/generate_badges', methods=['POST'])
@loginRequired
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
    badge_name = data.get('badge_name') or 'My Badge'
    image_name = data.get('image')
    font_color_1 = data.get('font_color_1') or '#ffffff'
    font_color_2 = data.get('font_color_2') or '#ffffff'
    font_color_3 = data.get('font_color_3') or '#ffffff'
    font_color_4 = data.get('font_color_4') or '#ffffff'
    font_color_5 = data.get('font_color_5') or '#ffffff'
    paper_size = data.get('paper_size') or 'A3'
    badge_size = data.get('badge_size') or '4x3'
    font_size_1 = data.get('font_size_1') or None
    font_size_2 = data.get('font_size_2') or None
    font_size_3 = data.get('font_size_3') or None
    font_size_4 = data.get('font_size_4') or None
    font_size_5 = data.get('font_size_5') or None
    font_type_1 = data.get('font_type_1') or 'helvetica'
    font_type_2 = data.get('font_type_2') or 'helvetica'
    font_type_3 = data.get('font_type_3') or 'helvetica'
    font_type_4 = data.get('font_type_4') or 'helvetica'
    font_type_5 = data.get('font_type_5') or 'helvetica'
    svg2png = SVG2PNG()

    if config.ENV == 'PROD':
        svg2png.do_text_fill(
            os.getcwd() + '/api/static/badges/8BadgesOnA3.svg',
            font_color_1,
            font_color_2,
            font_color_3,
            font_color_4,
            font_color_5,
            badge_size,
            paper_size)

        svg2png.change_font_size(
            os.getcwd() + '/api/static/badges/8BadgesOnA3.svg',
            badge_size,
            paper_size,
            font_size_1,
            font_size_2,
            font_size_3,
            font_size_4,
            font_size_5)

        svg2png.change_font_family(
            os.getcwd() + '/api/static/badges/8BadgesOnA3.svg',
            badge_size,
            paper_size,
            font_type_1,
            font_type_2,
            font_type_3,
            font_type_4,
            font_type_5)
    else:
        svg2png.do_text_fill(
            'static/badges/8BadgesOnA3.svg',
            font_color_1,
            font_color_2,
            font_color_3,
            font_color_4,
            font_color_5,
            badge_size,
            paper_size)

        svg2png.change_font_size(
            'static/badges/8BadgesOnA3.svg',
            badge_size,
            paper_size,
            font_size_1,
            font_size_2,
            font_size_3,
            font_size_4,
            font_size_5)

        svg2png.change_font_family(
            os.getcwd() + '/api/static/badges/8BadgesOnA3.svg',
            badge_size,
            paper_size,
            font_type_1,
            font_type_2,
            font_type_3,
            font_type_4,
            font_type_5)

    merge_badges = MergeBadges(
        image_name,
        csv_name,
        paper_size,
        badge_size)

    merge_badges.merge_pdfs()

    uid = data.get('uid')
    user_creator = User.getUser(user_id=uid)

    if user_creator.allowed_usage == 0:
        return ErrorResponse(UsageNotAllowed().message, 403, {'Content-Type': 'application/json'}).respond()

    user_creator.allowed_usage = user_creator.allowed_usage - 1

    badge_created = Badges(image=image_name, csv=csv_name,
                           text_color=font_color_1, badge_size=badge_size,
                           badge_name=badge_name, creator=user_creator)

    badge_created.save_to_db()

    badgeFolder = badge_created.image.split('.')[0]
    badgePath = ''
    if config.ENV == 'LOCAL':
        badgePath = os.getcwd() + '/static/temporary/' + badgeFolder
    else:
        badgePath = os.getcwd() + '/api/static/temporary/' + badgeFolder
    if os.path.isdir(badgePath):
        imageDirectory = os.path.join(
            badgePath, '../../uploads/image', image_name)
        link = fileUploader(imageDirectory, 'images/' + image_name)
        badge_created.image_link = link
        link = fileUploader(badgePath + '/all-badges.pdf',
                            'badges/' + badge_created.id + '.pdf')
        send_badge_mail(badge_created.id, user_creator.id, link)
        badge_created.download_link = link
        rmtree(badgePath, ignore_errors=True)

    db.session.commit()

    return jsonify(BadgeSchema().dump(badge_created).data)


def send_badge_mail(badgeId, userId, badgeLink):
    ref = firebase_db.reference('badgeMails')
    print('Pushing badge generation mail to : ', badgeId)
    ref.child(userId).child(datetime.datetime.utcnow().isoformat().replace('-', '_').replace(':', 'U').replace('.', 'D')).set({
        'badgeId': badgeId,
        'badgeLink': badgeLink
    })
    print('Pushed badge generation mail to : ', badgeId)


@router.route('/get_badges', methods=['GET'])
@loginRequired
def get_badges():
    input_data = request.args
    page = request.args.get('page', 1, type=int)
    user = User.getUser(user_id=input_data.get('uid'))
    badges = db.session.query(Badges).filter_by(creator=user).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    return jsonify(UserBadges(many=True).dump(badges.items).data)


@router.route('/get_badges/<badgeId>', methods=['DELETE'])
@loginRequired
def delete_badge(badgeId):
    badge = Badges.getBadge(badgeId)
    temp_badge = badge
    if not badge:
        print('No badge found with the specified ID')

    deleteFile('badges/' + badgeId + '.pdf')
    badge.delete_from_db()
    return jsonify(DeletedBadges().dump(temp_badge).data)


@router.route('/get_badges/<badgeId>', methods=['PATCH'])
@loginRequired
def change_name(badgeId):
    data = request.get_json()['data']['attributes']
    badge = Badges.getBadge(badgeId)
    badge.badge_name = data['badge-name']
    badge.save_to_db()
    return jsonify(BadgeSchema().dump(badge).data)
