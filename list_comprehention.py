# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

# nums = [i for i in range(1, 11)]
# for i in nums:
#     print(i, end=' ')
# print()


# my_list = [n*n for n in nums]
# my_list = map(lambda n: n*n, nums)
# my_list = [n for n in nums if n%2 == 0]
# my_list = filter(lambda n: n%2 == 0, nums)

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# my_list = zip(names, heroes)

# print(my_list)

# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero

# my_dict = {name:hero for name, hero in zip(names, heroes) if name <> 'Peter'}
#
# print my_dict


# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)

# my_set = {n  for n in nums}

# print my_set


nums = [i for i in range(1, 11)]

# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
#

my_gen = (n*n for n in nums)

for i in my_gen:
    print i,

