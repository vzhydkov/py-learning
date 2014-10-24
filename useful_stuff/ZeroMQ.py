# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import zmq
import time
from random import choice
from threading import Thread
try:
    from Queue import Queue
except ImportError:
    from queue import Queue


class Publish():
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind('tcp://127.0.0.1:5000')

    def start(self):
        messages = ['message1', 'message2', 'message3', 'message4']
        while True:
            time.sleep(2)
            message = choice(messages)
            self.socket.send(message)
            print('sent message: %s' % message)


class Subscribe():
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:5000')
        self.socket.setsockopt(zmq.SUBSCRIBE, 'message1')
        self.socket.setsockopt(zmq.SUBSCRIBE, 'message4')

    def start(self):
        while True:
            print('caught message: %s' % self.socket.recv())


class MyQueue():
    def __init__(self, queue):
        self.queue = queue

    def job(self, tread_id):
        while not self.queue.empty():
            print('Tread started: %s' % tread_id)
            task = self.queue.get()
            task.start()
            self.queue.task_done()

    def set_job(self, func):
        self.queue.put(func)

if __name__ == '__main__':
    myQueue = MyQueue(Queue())
    myQueue.set_job(Publish())
    myQueue.set_job(Subscribe())

    for tread_id in range(myQueue.queue.qsize()):
        Thread(target=myQueue.job, args=(tread_id, )).start()

    myQueue.queue.join()