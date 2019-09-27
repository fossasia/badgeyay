import os
import base64
import uuid
from flask import request, Blueprint, jsonify
from flask import current_app as app
from backend.models.file import File
from backend.schemas.file import ExportFileSchema
from backend.utils.errors import ErrorResponse
from backend.schemas.errors import (
    FileNotFound
)

router = Blueprint('exportData', __name__)

@router.route('/csv/data', methods=['GET'])
def export_data():
    input_data = request.args
    file = File().query.filter_by(filename=input_data.get('filename')).first()

    if file is None:
        return ErrorResponse(FileNotFound(input_data.get('filename')).message, 422, {'Content-Type': 'application/json'}).respond()

    export_obj = {
        'filename': file.filename,
        'filetype': file.filetype,
        'id': str(uuid.uuid4()),
        'file_data': None}

    with open(os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv', export_obj['filename']), "r") as f:
        export_obj['file_data'] = f.read()

    export_obj['file_data'] = base64.b64encode(export_obj['file_data'].encode())

    return jsonify(ExportFileSchema().dump(export_obj).data)
