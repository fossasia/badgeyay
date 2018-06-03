from flask import Blueprint, send_from_directory
from flask import current_app as app


router = Blueprint('staticHelper', __name__)


@router.route('/badges/<filename>.pdf')
def get_badge(filename):
    return send_from_directory(app.static_folder + '/badges', filename + '.pdf')
