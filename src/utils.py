def deco(color):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f"[{color.upper()}] --- START ---")
            result = func(*args, **kwargs)
            print(f"[{color.upper()}] --- END ---")
            return result
        return inner
    return wrapper
