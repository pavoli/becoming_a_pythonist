# coding: utf-8
__author__ = 'polly'

'''
создать папку
в папку записать фалйы разных форматов xls, doc, txt, mp3
создать программу, которая будет смотреть эту папку перечислением проходить по всем файлам этой папки
и если встречает программа в какой-то момент txt, то она его открывает и ищет в нем слово python.
выдает кол-во слов python в файле
'''

import os


def findTxt():
    for fileName in os.listdir('testFolder'):
        if fileName.endswith('.txt'):
            with open('testFolder/' + fileName) as f:
                py_qty = 0
                for line in f.readlines():
                    py_qty += line.count('python')
                print "file %s contains %d python words" % (fileName, py_qty)


if __name__ == '__main__':
    findTxt()
