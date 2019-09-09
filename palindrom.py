# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def is_poly(string: str) -> bool:
    d = Counter(string)
    # определяю четность или нечетность кол-ва букв
    return sum([d[i]%2 for i in d]) <= 1


str = 'asdasd113'
str_2 = 'sfsf'

print(is_poly(str))
