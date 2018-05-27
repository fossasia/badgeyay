from api.config import urlConfig
import uuid


class Response(object):
    """docstring for Response"""

    def __init__(self, statusCode):
        super(Response, self).__init__()
        self.status = statusCode

    def generateMessage(self, message, message_type, *args, **kwargs):
        self.id = uuid.uuid4()
        self.type = message_type
        if isinstance(message, dict):
            for key, value in iter(message.items()):
                self.attributes = {
                    key: value.format(*args, **kwargs)
                }
        else:
            self.attributes = {
                "message": message.format(*args, **kwargs)
            }
        return {'data': self.serialize()}

    def generateErrorMessage(self, message, message_type, *args, **kwargs):
        self.generateMessage(message, message_type, *args, **kwargs)
        return {'error': self.serialize()}

    def generateURL(self, url, message):
        self.message = message
        self.URL = url
        return self.sanitizeURL()

    def sanitizeURL(self):
        self.URL = self.URL.replace('backend/app/', urlConfig.BASE_URL)
        return {'data': self.serialize()}

    def generateResetURL(self, token):
        self.token = token
        self.URL = urlConfig.BASE_FRONTEND_URL + "reset/password/" + self.token
        return {'data': self.serialize()}

    def generateToken(self, token):
        self.token = token
        return {'data': self.serialize()}

    def exceptWithMessage(self, exception, message):
        self.message = message
        self.exception = exception
        return {'data': self.serialize()}

    def serialize(self):
        return self.__dict__
