# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

import sys


x = len(sys.argv)
if x>1:
    print('Arguments entered: {}'.format(sys.argv[1:]))
else:
    print('Arguments NOT provided...')