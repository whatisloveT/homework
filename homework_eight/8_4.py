from functools import wraps
def val_checker(i_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
                if i_func(num) > 0:
                    print(func(num))
                else:
                    raise ValueError(f'wrong val : {num}')

        return wrapper

    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(-5)