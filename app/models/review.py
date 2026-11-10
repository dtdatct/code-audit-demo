FIELDS = ('id', 'user_id', 'product_id', 'body')


class Review:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "Review(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
