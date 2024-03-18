class JuiceboxException(Exception):
    "Generic exception class for this library"
    pass

class InvalidMessageFormat(JuiceboxException):
    pass


class JuiceboxChecksumError(JuiceboxException):
    pass
