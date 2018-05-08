from api.config import urlConfig

class Response(object):
    """docstring for Response"""

    def __init__(self, statusCode):
        super(Response, self).__init__()
        self.status = statusCode

    def generateMessage(self, message):
        self.message = message
        return self.serialize()

    def generateURL(self, url, message):
        self.message = message
        self.URL = url
        return self.sanitizeURL()

    def sanitizeURL(self):
        self.URL = self.URL.replace('backend/app/', urlConfig.BASE_URL)
        return self.serialize()

    def generateToken(self, token):
        self.token = token
        return self.serialize()

    def serialize(self):
        return self.__dict__
