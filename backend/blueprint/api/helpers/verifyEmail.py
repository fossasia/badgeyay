import re
from flask import jsonify


def verifyEmail(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        return jsonify(
            Response(403).generateMessage("Not an Email Address")

