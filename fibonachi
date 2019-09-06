# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


# Создать функцию, которая выведет N чисел Фибоначчи
from typing import List


def fibo(n: int) -> List[int]:
    s1 = [1, 1]
    pos_0 = 0
    pos_1 = 1
    if n <= 2:
        return [1] * n
    else:
        for i in range(2, n):
            s1.append(s1[pos_0] + s1[pos_1])
            pos_0 += 1
            pos_1 += 1
    print(s1)
    return s1


assert [1, 1, 2, 3, 5, 8, 13, 21] == fibo(8)
