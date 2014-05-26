def parseint(str, type=None):
    try:
        if type == 10:
            return int(str)
        elif type == 8:
            return oct(int(str))
        elif type == 16:
            return hex(int(str))
        elif type == 2:
            return bin(int(str))
        else:
            return None
    except ValueError:
        return None

def do_task10():
    print('task10')
    print(parseint('foo', 'bin'))
    print(parseint('12', 'oct'))
    print(parseint('8', 16))
    print(parseint('6', 2))


if __name__ == "__main__":
    do_task10()
