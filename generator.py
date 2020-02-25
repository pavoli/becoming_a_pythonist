# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def simple_generator(val):
    while val > 0:
        val -= 1
        yield val

get_iter = simple_generator(5)
print(next(get_iter))
print(next(get_iter))
print(next(get_iter))
print(next(get_iter))
print(next(get_iter))