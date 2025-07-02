try:
    1/0
except ZeroDivisionError as e:
    print(f"Error Type:{type(e).__name__},message : {e}")
