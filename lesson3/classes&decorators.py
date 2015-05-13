from itertools import groupby
from datetime import date


def htmlize(par):
    if callable(par):
        def wrapper(self):
            res = par(self)
            return '<a href="%s">%s</a>' % (res, res)
        return wrapper
    else:
        def wrapper_params(fn):
            def wrapper(self):
                res = fn(self)
                return '<a class="%s" href="%s">%s</a>' % (par, res, res)
            return wrapper
        return wrapper_params

class Order(list):
    _total_orders = 0

    def __init__(self):
        self._discount = 0

    def append(self, item):
        self.date = date.today()
        self.__class__._total_orders += 1
        super(Order, self).append(item)

    @classmethod
    def get_total_orders(cls):
        return cls._total_orders

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 99:
            self._discount = value

    @property
    def total_price(self):
        price = 0.0
        for i in self:
            price += i.price
        return price - (price / 100 * self._discount)

    def get_files(self):
        yield [i for i in self if isinstance(i, DownloadableItem)]

    def __str__(self):
        result = ''
        sorted_orders = sorted(self, key=lambda x: x.name)
        for name, group in groupby(sorted_orders, key=lambda x: x.name):
            lst = list(group)
            result += 'Item name: %s, quantity of items: %d, total price: %d\n'\
                      % (name, len(lst), sum(row.price for row in lst))
        return result

class Item(object):
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class DownloadableItem(Item):
    downloads_count = 0

    def __init__(self, id, name, description, price, filename):
        self.filename = filename
        super(DownloadableItem, self).__init__(id, name, description, price)

    @classmethod
    def increment_downloads_count(cls):
        cls.downloads_count += 1

    @htmlize('my_class')
    def get_url(self):
        self.increment_downloads_count()
        return self.filename


if __name__ == "__main__":
    item1 = Item(1, 'htc', 'sux1', 1)
    item2 = Item(2, 'nokia', 'dead', 10)
    item3 = DownloadableItem(3, 'iphone', 'gold', 99, 'file3')
    item4 = DownloadableItem(4, 'htc', 'sux2', 1, 'file4')

    print('Url: %s' % item3.get_url())
    print('Url: %s' % item3.get_url())
    print('Url: %s' % item4.get_url())
    print('Downloads count: %d' % DownloadableItem.downloads_count)

    order = Order()
    order.discount = 50
    order.append(item1)
    order.append(item2)
    order.append(item3)
    order.append(item4)

    print('Orders: \n%s' % order)
    print('Total price: %d' % order.total_price)
    print('Total orders: %d' % order.get_total_orders())
    print('Order date: %s' % order.date)
    print(order.get_files())
