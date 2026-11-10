FIELDS = ('id', 'user_id', 'total', 'status')


class Order:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "Order(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
