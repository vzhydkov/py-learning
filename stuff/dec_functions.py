""" Decorators with or without arguments """

import functools


def decorator1(fn_or_dec_arg):
    """
    Simplest variant
    - No need to use named args for decorator
    - Different wrapper's for decorator with and without arguments
    - Decorator argument can't be a function
    """
    if callable(fn_or_dec_arg):
        # in this case fn_or_dec_arg is original function
        @functools.wraps(fn_or_dec_arg)
        def wrapper(*args, **kwargs):
            return '#dec#' + fn_or_dec_arg(*args, **kwargs)
        return wrapper
    else:
        # in this case fn_or_dec_arg in decorator argument
        def fn_wrapper(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kwargs):
                return '#dec#' + fn_or_dec_arg + fn(*args, **kwargs)
            return wrapper
        return fn_wrapper


def decorator2(fn=None, dec_arg=''):
    """
    - Named arguments for decorator
    - One wrapper for both cases
    - Function can be passed as decorator argument
    """
    def fn_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return '#dec#' + dec_arg + fn(*args, **kwargs)
        return wrapper
    if fn is not None:
        return fn_wrapper(fn)
    return fn_wrapper


def decorator3(fn=None, dec_arg=''):
    """
    If called without method, we've been called with optional arguments.
    We return a decorator with the optional arguments filled in.
    Next time round we'll be decorating method.
    """
    if fn is None:
        return functools.partial(decorator3, dec_arg=dec_arg)

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return '#dec#' + dec_arg + fn(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    """
    def func1(arg):
        return arg
    func1 = decorator1('#dec_arg#')(func1)
    func1 = decorator1(func1)
    """
    @decorator1  # will be called second
    @decorator1('#dec_arg#')  # will be called first
    def func1(fn_arg):
        return fn_arg

    assert func1.__name__ == 'func1'

    @decorator2
    @decorator2(dec_arg='#dec_arg#')
    def func2(fn_arg):
        return fn_arg

    assert func2.__name__ == 'func2'

    @decorator3
    @decorator3(dec_arg='#dec_arg#')
    def func3(fn_arg):
        return fn_arg

    assert func3.__name__ == 'func3'

    assert func1('#fn_arg#') == func2('#fn_arg#') == func3('#fn_arg#')
