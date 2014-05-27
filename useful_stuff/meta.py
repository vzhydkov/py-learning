# class C: pass
# its:
# C = type('C', (), {})

class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print(Meta, ' __new__')
        return super(Meta, meta).__new__(meta, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict):
        print(Meta, ' __init__')
        super(Meta, cls).__init__(classname, supers, classdict)
        #type.__init__(cls, name, bases, dct) # call type __ini__


def MetaFunc(classname, supers, classdict):
    print(MetaFunc, '__new__')
    return type(classname, supers, classdict)


class Spam(metaclass=Meta):
    #__metaclass__ = Meta  # py2
    def __new__(cls, *args, **kwargs):
        print(Spam, ' __new__')
        return super(Spam, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print(Spam, ' __init__')


print('making instance')
X = Spam()


""" singleton """
class Singleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if not cls.instance:
             cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class ASingleton(object, metaclass=Singleton):
    # __metaclass__ = Singleton


a = ASingleton()
b = ASingleton()
assert a is b
