def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj is an instance of a subclass of a_class, otherwise False.
    """
    if isinstance(obj, type):
        return issubclass(obj, a_class)
    return isinstance(obj, a_class)
