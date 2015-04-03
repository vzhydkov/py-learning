import time
import functools


def benchmark(func):
    """
    Decorator time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print('Benchmark:', time.clock() - t, '(sec)')
        return res
    return wrapper


def logging(func):
    """
    Decorator logger
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('Logging:', func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    """
    Decorator counter
    """
    counter.count[func.__name__] = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        counter.count[func.__name__] += 1
        res = func(*args, **kwargs)
        print('Counter: {0} was called: {1}x'.format(func.__name__, counter.count[func.__name__]))
        return res
    return wrapper


def timer(label='', trace=True):
    def on_decorator(func):
        @functools.wraps(func)
        def on_call(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            on_call.all_time += elapsed
            if trace:
                values = (label, func.__name__, elapsed, on_call.all_time)
                print('Timer %s%s: %.5f, %.5f' % values)
            return result
        on_call.all_time = 0
        return on_call
    return on_decorator

if __name__ == "__main__":
    counter.count = {}

    @benchmark
    @logging
    @counter
    @timer()
    def reverse_string(string):
        return string[::-1]
        # return ''.join(reversed(string))

    print(reverse_string('a b c'))
