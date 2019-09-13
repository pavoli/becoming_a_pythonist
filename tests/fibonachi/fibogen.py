# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def fibogen(n):
    if type(n) is not int:
        raise TypeError('type of argument should be int!')
    if n <= 0:
        return
    else:
        f1 = 0
        f2 = 1
        yield 1
        for i in range(2, n):
            result = f1 + f2
            f1 = f2
            f2 = result
            yield result


if __name__ == '__main__':
    # for i in fib_gen(10):
    #     print(i)
    print(list(fibogen(10)))