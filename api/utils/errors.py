from flask import make_response, jsonify


class ErrorResponse():

    """
    Parent ErrorResponse class for handling json-api compliant errors
    """

    def __init__(self, message, status_code, content_type):
        self.message = message
        self.status_code = status_code
        self.content_type = content_type

    def respond(self):
        """
        :return: a jsonapi compliant response object
        """
        return make_response(jsonify(self.message), self.status_code, self.content_type)
