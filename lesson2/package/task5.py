def do_task5():
    print('task5')
    import os
    with open(os.path.dirname(__file__)+"/task5.txt", "r+") as f:
        res = f.read().replace('PHP', 'Python')
        f.seek(0)
        f.write(res)
        f.truncate()

if __name__ == "__main__":
    do_task5()