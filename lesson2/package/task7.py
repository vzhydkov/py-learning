def do_task7():
    print('task7')
    lists = [[1, 2, 3, 4],
        [2, 4, 4, 2],
        [6],
        [1, 1, 1, 1, 1]]
    print(list(map(max, *lists)))

if __name__ == "__main__":
    do_task7()