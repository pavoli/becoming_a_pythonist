# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('Hi')
hello_func = outer_func('Hello')


hi_func()
hello_func()