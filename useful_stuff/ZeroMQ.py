# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import zmqпше
import time
from random import choice
from threading import Thread


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

if __name__ == '__main__':
    for tread_id, task in enumerate((Publish, Subscribe)):
        print('Tread started: %s' % tread_id)
        Thread(target=task().start).start()
