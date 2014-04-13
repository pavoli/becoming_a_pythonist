# coding: utf-8
__author__ = 'polly'

'''
merge sort
'''


def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def merge_sort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length/2)
        lst = merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
    return lst

lst = [10, 3, 2, 79, 10, 0, 12, 11, 15, -4, 0]
print merge_sort(lst)

