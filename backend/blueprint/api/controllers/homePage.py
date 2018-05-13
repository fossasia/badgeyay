from flask import Blueprint, jsonify
from utils.response import Response
from flasgger.utils import swag_from

router = Blueprint('homePage', __name__)


@router.route('/', methods=['GET', 'POST'])
def homePage():
    """
    Return API status.
    ---
    tags:
      - HomePage
    responses:
      200:
        description: This is the homepage route. Please follow /api/generate_badges for badge creation
    """
    return jsonify(
        Response(200).generateMessage(
            'This is the homepage route. Please follow /api/generate_badges for badge creation'))
