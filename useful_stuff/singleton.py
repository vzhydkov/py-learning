class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass

if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    assert a is b

    a = MyClass()
    b = MyClass()
    assert a is b







