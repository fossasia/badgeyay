class Response(object):
    """docstring for Response"""
    def __init__(self, statusCode):
        super(Response, self).__init__()
        self.status = statusCode
        self.message = None
        self.response = {
            'status': self.status
        }

    def generateMessage(self, message):
        self.message = message
        self.response['message'] = self.message

        return self.response
