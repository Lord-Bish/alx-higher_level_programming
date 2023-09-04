#!/usr/bin/python3
def safe_print_division(a, b):
    result = a / b

    try:
        result
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("inside result: {:d}".format(result))
    return (result)
