def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        print("{:d} / {:d} = {}".format(a, b, result))
        return result
    finally:
        print("Finally block executed.")
        
print(safe_print_division(10,b))