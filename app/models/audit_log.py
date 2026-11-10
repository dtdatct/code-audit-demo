FIELDS = ('id', 'actor', 'action', 'detail')


class AuditLog:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "AuditLog(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
