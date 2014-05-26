def show_sum_args(*args):
    if all( isinstance(i, int) for i in args):
        print(sum(args))
    else:
        raise TypeError('Invalid param')


def do_task9():
    print('task9')
    show_sum_args(1, 2, 3, 4)
    show_sum_args(1, 2, 3, '4')

if __name__ == "__main__":
    do_task9()