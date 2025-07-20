def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m",
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            color_code = colors.get(color, "")
            reset_code = colors["reset"]
            print(color_code, end="")  # включаем цвет
            result = func(*args, **kwargs)
            print(reset_code, end="")  # сбрасываем цвет
            return result
        return wrapper
    return decorator
