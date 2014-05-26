# -*- coding: utf-8 -*-

def do_task6():
    print('task6')
    unicode_str = b'абвг'.decode("utf-8")
    print(sum(ord(c) for c in unicode_str))


if __name__ == "__main__":
    do_task6()