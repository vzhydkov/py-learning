def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta('NewBase', bases, {})


class Meta(type):
    """Example of singleton meta"""
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Meta, cls).__call__(*args, **kwargs)
        return cls.instance


class SingletonMeta(with_metaclass(Meta, object)):
    pass


class SingletonClass(object):
    """Example of singleton class"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def singleton(cls):
    """Example of singleton decorator"""
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class SingletonDecorator:
    pass


if __name__ == '__main__':
    a = SingletonMeta()
    b = SingletonMeta()
    assert a is b

    a = SingletonClass()
    b = SingletonClass()
    assert a is b

    a = SingletonDecorator()
    b = SingletonDecorator()
    assert a is b
