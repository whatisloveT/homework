from functools import wraps
def type_logger(func):
        @wraps(func)
        def wrapper(*args):
            for a in args:
                print(f'{func.__name__} ({a}: {type(a)})')

        return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


a = calc_cube(-5,3,7.2)