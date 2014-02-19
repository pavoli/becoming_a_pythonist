__author__ = 'polly'

"""
Как получить список всех атрибутов объекта
"""
dir(obj)


"""
Как получить список всех публичных атрибутов объекта
"""
#1
[a for a in dir(obj) if not a.startswith('_')]


#2
filter(lambda x: x.startswith('_'), dir(obj))


"""
Как получить список методов объекта
"""
#1
[a for a in dir(obj) if callable(getattr(obj, a))]


#2
filter(lambda x: callable(getattr(obj, x)), dir(obj))


"""
В какой "магической" переменной хранится содержимое help?
"""
obj.__doc__


"""
Есть два кортежа, получить третий как конкатенацию первых двух
"""
(1,3) + (4,6)


"""
Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей
"""
tuple(set((3,4)) ^ set((4,5)))


"""
Есть два списка одинаковой длины, в одном ключи, в другом значения. Составить словарь.
"""
keys = [1, 3, 5]
values = [0, 2, 4]
dictionary = dict(zip(keys, values))


"""
Есть словарь. Инвертировать его. Т.е. пары ключ: значение поменять местами — значение: ключ.
"""
dictionary = {'key0': 'value0', 'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#1
temp = dictionary.items()
dictionary.clear()
for key, value in temp:
    dictionary[value] = key

#2
dict(zip(d1.values(), d1.keys()))

print dictionary


"""
Написать функцию-генератор cycle которая бы возвращала циклический итератор.
"""
def cycle(val):
    c = [i for i in val]
    while 1:
        for y in c:
            yield y


"""
Написать функцию-генератор chain, которая последовательно итерирует переданные объекты (произвольное количество)
"""
from __future__ import generators

def chain(*args):
    for x in args:
        for element in x:
            yield element
            
            
"""
Как посмотреть список каталогов, в которых Python ищет модули?
"""
import sys
for p in sys.path:
    print p


"""

"""
