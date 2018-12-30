import threading


# make a new thread
def thread(fn):
    def wrapper(*args, **kwargs):
        new_thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        new_thread.start()
    return wrapper


@thread
def run(id):
    for i in range(1, 100):
        print('thread', id, 'number', i)

if __name__ == "__main__":
    run(1)
    run(2)
    run(3)
