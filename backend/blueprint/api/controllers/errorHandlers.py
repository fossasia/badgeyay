from flask import Blueprint, jsonify
from api.utils.response import Response

router = Blueprint('errorHandler', __name__)


@router.app_errorhandler(404)
def handle_404(err):
    return jsonify(
        Response(404).generateMessage(
            str(err)))


@router.app_errorhandler(500)
def handle_500(err):
    return jsonify(
        Response(500).generateMessage(
            str(err)))
