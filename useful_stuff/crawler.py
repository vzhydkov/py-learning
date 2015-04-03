"""
pip install cssselect
"""

from datetime import datetime
try:
    from Queue import Queue
except ImportError:
    from queue import Queue
from threading import Thread
from lxml.html import parse


class Crawler():
    def __init__(self, queue, available_depth=50):
        self.queue = queue
        self.available_depth = available_depth
        self.current_depth = 0

    def job(self, tread_id):
        while not self.queue.empty():
            item = self.queue.get()
            try:
                start = datetime.now()
                page = parse(item).getroot()
                if page is not None:
                    for link in page.cssselect('a'):
                        self.set_job(link.get('href'))
                    images = len(page.cssselect('img'))
                    elapsed = datetime.now() - start
                    print('Thread-%d: %s (%d images) %d.%d' %
                          (tread_id, item, images, elapsed.seconds, elapsed.microseconds))
            except IOError:
                print('Thread %d: not a real URL: %s' % (tread_id, item))
            self.queue.task_done()

    def set_job(self, url):
        if self.current_depth < self.available_depth:
            self.queue.put(url)
            self.current_depth += 1

crawler = Crawler(Queue())
crawler.set_job('http://sfw.so')
crawler.set_job('http://itc.ua')

for tread_id in range(crawler.queue.qsize()):
    tread = Thread(target=crawler.job, args=(tread_id, ))
    tread.daemon = True
    tread.start()

crawler.queue.join()

# need add checking "netloc"
# from urlparse import urlparse
# print urlparse(url)