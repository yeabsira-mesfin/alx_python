def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    :param obj: The object to be checked.
    :param a_class: The class to compare against.
    :return: True if the object is an instance of the specified class or its subclass, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    # Check if any base class of obj is an instance of a_class
    for base_class in obj.__class__.mro():
        if base_class == a_class:
            return True
    return False