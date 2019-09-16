# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from urllib import request

myUrl = 'http://www.astahov.net'

myAnswer = request.urlopen(myUrl)
myText1 = myAnswer.readlines()
myText2 = myAnswer.read()

print(myAnswer)

for i in myText1:
    print(i)
print(myText2)