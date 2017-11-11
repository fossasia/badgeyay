class PackageNotFoundError(Exception):
    """
    Exception class for Package not found
    :param `Exception` - Exception parameter passed
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
