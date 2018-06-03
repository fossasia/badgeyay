from marshmallow_jsonapi.exceptions import JSONAPIError


class BaseError(JSONAPIError, ValueError):

    def __init__(self, uid=None, attr=None, status=422):
        self.pointer = '/data/attributes/{0}'.format(attr)
        if uid:
            self.detail = '{0} not found : {1}'.format(attr, uid)
        else:
            self.detail = '{0} not found'.format(attr)
        if attr == 'operation':
            self.detail = 'Operation not successful'
        elif attr == 'extension':
            self.detail = 'No extension key received'
        elif attr == 'manual_data':
            self.detail = 'No Manual Data is specified'
        elif attr == 'json':
            self.detail = 'Unable to get JSON'
        elif attr == 'pass':
            self.detail = 'Wrong username and password combination'
        self.status = status
        super(BaseError, self).__init__(self.detail, self.pointer, self.status)

    @property
    def message(self):
        return {
            'errors': [
                {
                    'detail': self.detail,
                    'status': self.status,
                    'source': {
                        'pointer': self.pointer
                    }
                }
            ]
        }


class UserNotFound(BaseError):

    def __init__(self, uid):
        super(UserNotFound, self).__init__(uid=uid, attr='user')


class FileNotFound(BaseError):

    def __init__(self, uid):
        super(FileNotFound, self).__init__(uid=uid, attr='file')


class BadgeNotFound(BaseError):

    def __init__(self, uid):
        super(BadgeNotFound, self).__init__(uid=uid, attr='badge')


class PayloadNotFound(BaseError):

    def __init__(self):
        super(PayloadNotFound, self).__init__(attr='payload')


class CSVNotFound(BaseError):

    def __init__(self):
        super(CSVNotFound, self).__init__(attr='csv')


class ImageNotFound(BaseError):

    def __init__(self):
        super(ImageNotFound, self).__init__(attr='image')


class OperationNotFound(BaseError):

    def __init__(self):
        super(OperationNotFound, self).__init__(attr='operation')


class ExtensionNotFound(BaseError):

    def __init__(self):
        super(ExtensionNotFound, self).__init__(attr='extension')


class ManualDataNotFound(BaseError):

    def __init__(self):
        super(ManualDataNotFound, self).__init__(attr='manual_data')


class JsonNotFound(BaseError):

    def __init__(self):
        super(JsonNotFound, self).__init__(attr='json')


class PasswordNotFound(BaseError):

    def __init__(self):
        super(PasswordNotFound, self).__init__(attr='pass')
