# class C: pass
# C = type('C', (), {})
# NewType = type("NewType", (object,), {"x": "hello"})

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})

class Meta(type):
    def __new__(meta, name, bases, attrs):
        print(Meta, ' __new__')
        return super(Meta, meta).__new__(meta, name, bases, attrs)
        #return type.__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print(Meta, ' __init__')
        super(Meta, cls).__init__(name, bases, attrs)
        #type.__init__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(Meta, ' __call__')
        return super(Meta, cls).__call__(*args, **kwargs)
        #return type.__call__(cls, *args, **kwargs)


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


class Singleton(type):
    """Example of singleton"""
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class ASingleton(with_metaclass(Singleton, object)):
    pass

a = ASingleton()
b = ASingleton()
assert a is b
