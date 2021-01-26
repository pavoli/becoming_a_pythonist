# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


iter1 = SimpleIterator(3)
print(next(iter1))
print(next(iter1))
print(next(iter1))

iter2 = SimpleIterator(5)
for i in iter2:
    print(i)
