# coding: utf-8
__author__ = 'polly'

import re

p = r'(((0[1-9])|(1[0-9])|(3[0-1]))\.((0[1-9])|(1[0-2]))\.[0-9]{4})'
num = re.compile(p)
print num.findall('31.19.1984')
print num.findall('31.09.1984')
