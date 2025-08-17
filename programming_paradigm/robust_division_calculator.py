def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        div = numerator / denominator
        return f"Result is {div}"
    except ZeroDivisionError:
        return f"Error: can't divide by zero"
    except ValueError:
        return f"Error: non-numerical value"
    

