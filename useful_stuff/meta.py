class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print(Meta, ' __new__')
        return super(Meta, meta).__new__(meta, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict):
        print(Meta, ' __init__')
        super(Meta, cls).__init__(classname, supers, classdict)


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