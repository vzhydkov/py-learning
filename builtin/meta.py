"""
class C: pass
class = type("classname", superclasses, attributedict)
NewType = type("NewType", (object,), {"x": "hello"})
"""


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        return type.__new__(mcs, name, bases, attrs)
        # return super(Meta, meta).__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        # super(Meta, cls).__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        return type.__call__(cls, *args, **kwargs)
        # return super(Meta, cls).__call__(*args, **kwargs)


class NewClass(with_metaclass(Meta, object)):
    pass
