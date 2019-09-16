# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


from urllib import request
import sys


my_url = 'http://adv400.tripod.com/kartinka.jpg'
my_file_path = 'C:\\Users\\p.olifer\\Downloads\\my_pic.jpg'

try:
    print('Start Downloading file from: {}'.format(my_url))
    request.urlretrieve(my_url, my_file_path)
except Exception:
    print('Achtung!!!')
    print(sys.exc_info()[1])

print('File Downloaded and SAVED at: {}'.format(my_file_path))