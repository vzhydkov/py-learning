import functools


class DecNoArgs(object):
    def __init__(self, fn):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        self.fn = fn

    def __get__(self, obj, tp=None):
        """
        self.__class__.__name__ will give you the name of the class,
        but you can also use descriptors to accomplish this
        in a somewhat more general way.
        """
        return self.__class__(self.fn.__get__(obj, tp))

    def __call__(self, *args, **kw):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        return self.fn(*args, **kw)


class DecWithArgs(object):
    def __init__(self, *args, **kwargs):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.dec_args = args
        self.dec_kwargs = kwargs

    def __call__(self, fn):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper


if __name__ == "__main__":
    class Class1(object):
        @DecNoArgs
        def func1(self, *args, **kwargs):
            return args, kwargs

    @DecNoArgs
    def func1(*args, **kwargs):
        return args, kwargs

    class Class2(object):
        @DecWithArgs('dec_arg')
        def func2(self, *args, **kwargs):
            return args, kwargs

    @DecWithArgs('dec_arg')
    def func2(*args, **kwargs):
        return args, kwargs

    assert Class1().func1('arg') == func1('arg')
    assert Class2().func2('arg') == func2('arg')
