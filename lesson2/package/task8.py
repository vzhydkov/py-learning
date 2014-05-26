def do_task8():
    print('task8')
    import os
    with open(os.path.dirname(__file__)+"/task8.txt") as f:
        try:
            exec(f.read()) #compile
        except SyntaxError:
            print('catched syntax error in file')


if __name__ == "__main__":
    do_task8()


