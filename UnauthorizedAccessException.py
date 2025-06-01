# the exception clas only handling UnauthorizedAccessException

class UnauthorizedAccessException(Exception):
    def __init__(self, *args):
        super().__init__(*args)