from api.config import urlConfig
import uuid


class Response(object):
    """
    Send appropriate cleaned data that can be rendered into arbitrary media types.

    Function of the Response class is called with status code and other necessary formal arguments.
    Data is serialized and sent in a cleaned format that can be easily rendered.

    Required Parameter:
    statusCode: <int> - HTTP status code representing status of the Response.
    """

    def __init__(self, statusCode):
        """
        Constructor method to initialize the status code sent by the formal argument.
        """
        super(Response, self).__init__()
        self.status = statusCode

    def generateMessage(self, message):
        """
        Parameter:
        :message: <String> - Text message to be serialized.
        """
        self.id = uuid.uuid4()
        self.attributes = message
        self.type = 'imgResponse'
        return {'data': self.serialize()}

    def generateURL(self, url, message):
        """
        Parameter:
        :url: URL to be serialized. Sent as a String.
        :message: Text message.
        """
        self.message = message
        self.URL = url
        return self.sanitizeURL()

    def sanitizeURL(self):
        self.URL = self.URL.replace('backend/app/', urlConfig.BASE_URL)
        return {'data': self.serialize()}

    def generateResetURL(self, token):
        """
        Generate URL for password reset corresponding to a particular token.
        """
        self.token = token
        self.URL = urlConfig.BASE_FRONTEND_URL + "reset/password/" + self.token
        return {'data': self.serialize()}

    def generateToken(self, token):
        """
        Generate a HTTP response with the token and status code provided.
        """
        self.token = token
        return {'data': self.serialize()}

    def exceptWithMessage(self, exception, message):
        """
        Parameters:
        :exception: Exception caught.
        :message: Message to be serialized with the exception.
        """
        self.message = message
        self.exception = exception
        return {'data': self.serialize()}

    def serialize(self):
        """
        Serialize all the class variables in a dictionary.
        """
        return self.__dict__
