
def any(iterable):
    for element in iterable:
        if element in 'bob':
            return True
    return False


def do_task3():
    print('task3')

    a = set('bob')
    b = {'a', 'b', 'c'}
    # using any
    if any(b):
        print('String contains needed symbols')
    else:
        print('String does\'t contains needed symbols')

    # using intersection
    if a & b:
        print('String contains needed symbols')
    else:
        print('String does\'t contains needed symbols')


if __name__ == "__main__":
    do_task3()
