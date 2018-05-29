import jwt
import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
from api.utils.response import Response


router = Blueprint('oAuthToken', __name__)


@router.route('/oauth_token', methods=['POST'])
def oauth_token():
	try:
		data = request.get_json()
	except Exception as e:
		return jsonify(
			Response(401).exceptWithMessage(
				str(e),
				'No details found'))

	try:
		token = jwt.encode(
			{'user': data.get('username'),
				'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)},
			app.config.get('SECRET_KEY'))

	except Exception as e:
		return jsonify(
			Response(400).exceptWithMessage(
				str(e),
				'Token could not be generated'))
	return jsonify(
		Response(200).generateToken(
			token.decode('UTF-8')))
