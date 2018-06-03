from flask import Blueprint, jsonify
from api.utils.response import Response

router = Blueprint('homePage', __name__)


@router.route('/', methods=['POST'])
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
