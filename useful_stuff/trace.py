import sys
import time

"""Python 3"""
def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.clock()
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

if __name__ == "__main__" and sys.version_info[0] >= 3:
    class Person:
        @tracer
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay
        @timer()
        def getName(self):
            return self.name

    person1 = Person('Vitaliy', 3000)
    person1.getName()
    person2 = Person('Alex' ,1500)