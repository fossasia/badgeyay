from flask_mail import Mail, Message
from flask import current_app as app
from flask import jsonify
from models.user import User
from .response import Response


def send_mail(message):
    if message and message.receipent:
        user = User.getUser(message.receipent)
        if not user:
            return jsonify(
                Response(403).generateMessage(
                    'Couldn\'t find the username specified'))
        try:
            msg = Message(
                subject=message.subject,
                sender=app.config['MAIL_USERNAME'],
                recipients=[message.receipent],
                body=message.body)
            Mail(app).send(msg)
        except Exception as e:
            return jsonify(
                Response(500).exceptWithMessage(
                    str(e),
                    'Unable to send the mail'))
        return jsonify(
            Response(200).generateMessage(
                'Mail Sent'))
    else:
        return jsonify(
            Response(403).generateMessage(
                'No data received'))
