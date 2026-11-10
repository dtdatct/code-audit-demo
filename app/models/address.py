FIELDS = ('id', 'user_id', 'street', 'city', 'zip')


class Address:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "Address(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
