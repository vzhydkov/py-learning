def do_task4():
    print('task4')
    import os
    with open(os.path.dirname(__file__)+"/task4.txt") as f1:
        with open(os.path.dirname(__file__)+"/task4reversed.txt", "w") as f2:
            f2.writelines(reversed(f1.readlines()))


if __name__ == "__main__":
    do_task4()
