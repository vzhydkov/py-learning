import functools


class dec_no_args(object):
    def __init__(self, fn):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        self.fn = fn

    def __get__(self, obj, type=None):
        """
        self.__class__.__name__ will give you the name of the class,
        but you can also use descriptors to accomplish this
        in a somewhat more general way.
        """
        return self.__class__(self.fn.__get__(obj, type))

    def __call__(self, *args, **kw):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        return self.fn(*args, **kw)


class dec_with_args(object):
    def __init__(self, arg):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.arg = arg

    def __call__(self, fn):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        @functools.wraps(fn)
        def wrapper(*args):
            fn(*args)
        return wrapper


if __name__ == "__main__":
    class Class1(object):
        @dec_no_args
        def f(self, arg):
            return arg

    @dec_no_args
    def func1(arg):
        return arg

    class Class2(object):
        @dec_with_args('dec_arg')
        def func2(self, arg):
            return arg

    @dec_with_args("dec_arg")
    def func2(arg):
        return arg

