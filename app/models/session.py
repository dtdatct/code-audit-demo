FIELDS = ('id', 'token', 'user_id', 'created_at')


class Session:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "Session(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
