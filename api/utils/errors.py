from flask import Response, make_response, jsonify


class ErrorResponse(Response):

    """
    Parent ErrorResponse class for handling json-api compliant errors
    """

    def __init__(self, message, status_code, content_type, **kwargs):
        Response.__init__(self, **kwargs)
        self.message = message
        self.status_code = status_code
        self.content_type = content_type

    def respond(self):
        """
        :return: a jsonapi compliant response object
        """
        return make_response(jsonify(self.message), self.status_code, self.content_type)
