# class C: pass
# class = type("classname", superclasses, attributedict)
# NewType = type("NewType", (object,), {"x": "hello"})


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})


class Meta(type):
    def __new__(meta, name, bases, attrs):
        print(Meta, ' __new__')
        return type.__new__(meta, name, bases, attrs)
        # return super(Meta, meta).__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print(Meta, ' __init__')
        type.__init__(cls, name, bases, attrs)
        # super(Meta, cls).__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(Meta, ' __call__')
        return type.__call__(cls, *args, **kwargs)
        # return super(Meta, cls).__call__(*args, **kwargs)


def meta_func(name, bases, attrs):
    print(meta_func, '__new__')
    return type(name, bases, attrs)


class Spam(with_metaclass(Meta, object)):
    def __new__(cls, *args, **kwargs):
        print(Spam, ' __new__')
        return super(Spam, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print(Spam, ' __init__')


print('making instance')
spam = Spam()

