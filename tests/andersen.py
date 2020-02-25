# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

"""
print('1.')
print([1, 2] * 3)

a = []
b = {}
c = ()
print('2.')
print(a or b or c)
print(a and b and c)

t = {0: 1, 1: 2, 2: 3}
print('t={}'.format(t))
print('3.1.')
print(any(t))
print('3.2.')
print(all(t))

print('4.')
print(list(map(abs, [-1, 1, 0])))

print('5.')
print(sorted([('Alice', 2), ('Bob', 1), ('Charlie', -1)], key=lambda x: x[1]))

print('5.')
print(' '.join('123'))
"""

a = 1
b = 4

def f():
    # print(a)
    print(b)
    print(a + b)
    # b += 1
    print(a + b)

f()