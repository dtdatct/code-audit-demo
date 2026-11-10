FIELDS = ('id', 'name', 'price', 'sku')


class Product:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)   # mass assignment: any key from request JSON is accepted

    def __repr__(self):
        return "Product(" + repr(self.__dict__) + ")"   # dumps every field, secrets included, into logs
