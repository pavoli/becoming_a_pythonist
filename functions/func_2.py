# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi!')
log_hi()