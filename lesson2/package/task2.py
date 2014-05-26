def foo(param=None):
    if callable(param):
        param = param()
def bar(): pass


def do_task2():
    print('task2')
    foo(bar)


if __name__ == "__main__":
    do_task2()
