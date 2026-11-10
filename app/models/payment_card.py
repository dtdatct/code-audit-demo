FIELDS = ('id', 'user_id', 'pan', 'cvv', 'expiry')


class PaymentCard:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "PaymentCard(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
