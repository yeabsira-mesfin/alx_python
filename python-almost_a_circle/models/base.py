class Base:
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # Assign the public instance attribute id
        else:
            Base.__nb_objects += 1  # Increment the private class attribute
            self.id = Base.__nb_objects  # Assign the new value to the public instance attribute id
