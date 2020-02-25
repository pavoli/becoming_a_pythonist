# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

a = [0, 0, -5, 30212]
b = [-10, 40, -3, 9]
v = -10


def sum_of_two(a, b, v):
    return (any(v-i in b for i in a))


if __name__ == '__main__':
    print(sum_of_two(a, b, v))