# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def is_poly(string: str) -> bool:
    # построю словарь с кол-вом каждой буквы
    d = {}
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print('d={}'.format(d))
    # определяю четность или нечетность кол-ва букв
    dict_value = [d[i]%2 for i in d]
    print('dict_value={}'.format(dict_value))

    # если четное кол-во букв
    if (len(string) % 2 == 0):
        if (all(i == 0 for i in dict_value)):
            answer = True
        else:
            answer = False
    else:
        d_0 = [i for i in dict_value if i == 0]
        d_1 = [i for i in dict_value if i == 1]
        if (all(i == 0 for i in d_0) and len(d_1) == 1):
            answer = True
        else:
            answer = False
    return answer


str = 'asdasd113'
str_2 = 'sfsf'

print(is_poly(str))
