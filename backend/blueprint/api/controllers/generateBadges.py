from flask import Blueprint, jsonify
from utils.response import Response

router = Blueprint('generateBadges', __name__)


@router.route('/generate_badges', methods=['POST'])
def generateBadges():
    return jsonify(
        Response(200).generateMessage(
            'Use this route to generate badges from badgeyay'))
