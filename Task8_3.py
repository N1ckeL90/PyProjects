from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        result = callback(*args)
        if len(args) == 1:
            print(f'{callback.__name__}({args[0]}:{type(args[0])})')
        else:
            tmp = ''
            for el in args:
                tmp = tmp + f'{el}:{type(el)}, '
            list_args = f'{callback.__name__}({tmp})'
            print(f'{list_args[:-3]})')
        return result

    return wrapper


@type_logger
def calc_cube(*args):
    """calculating the cube of a number"""
    return args[0] ** 3


a = calc_cube(5)
print(a)
help(calc_cube)
