from flask_mail import Mail, Message
from flask import current_app as app
from flask import jsonify
from api.utils.response import Response


def sendMail(message):
    if message and message.receipent:
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
