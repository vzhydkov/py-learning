""" operator overloading methods """

""" @property """
class PropertyTest(object):
    def __init__(self, name):
        self._name = name
    @property
    def name(self):  # name = property(name)
        return self._name
    @name.setter
    def name(self, value):  # name = name.setter(name)
        self._name = value
    @name.deleter
    def name(self):  # name = name.deleter(name)
        del self._name

""" Descriptor """
class Descriptor(object):
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        instance._value = value
    def __delete__(self, instance):
        del instance._value


class Subject(object):
    def __init__(self):
        self._value = None
    value = Descriptor()


class Overloading(object):
    def __getattr__(self, name):  # x.undefined
        return self.__dict__[name]
    def __setattr__(self, name, value):  # x.any = value
        self.__dict__[name] = value
    def __delattr__(self, attr):  # del x.any
        del self.__dict__[attr]
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    def __call__(self, *args, **kwargs):  # x()
        return super(Overloading, self).__call__(*args, **kwargs)
