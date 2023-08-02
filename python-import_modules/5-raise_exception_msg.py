def raise_exception_msg(message=""):
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    if not message:
        raise NameError("An exception occurred with no specific message.")
    else:
        raise NameError(message)