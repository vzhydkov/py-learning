""" Python 3 only """

import functools


def tracer(func):
    calls = 0

    @functools.wraps(func)
    def on_call(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return on_call


if __name__ == "__main__":
    class Class1:
        @tracer
        def __init__(self):
            pass

    @tracer
    def func1():
        pass

    Class1()
    Class1()

    func1()
    func1()

