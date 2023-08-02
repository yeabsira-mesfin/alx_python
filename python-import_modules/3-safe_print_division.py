def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        # print("Error: Division by zero is not allowed.")
       
        return None
    # except Exception as e:
    #     # print(f"An unexpected error occurred: {e}")
    #     return None
    finally:
        print("Inside result: {}".format(result))