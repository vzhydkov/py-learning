class Class:
    @classmethod
    def class_method(cls):
        print('class_method')

    @staticmethod
    def static_method():
        print('static_method')

    def instance_method(self):
        print('instance_method')

instance = Class()

Class.class_method()
instance.class_method()

Class.static_method()
instance.static_method()

# Class.instance_method()  # TypeError
instance.instance_method()


""" property """
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):

        self._x = value
    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


""" decorators property """
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x