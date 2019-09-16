# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


from urllib import request, parse
import sys


my_url = 'http://www.google.com/search?'
my_value = {
    'q': 'ANDESA Soft',
}
my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

try:
    my_data = parse.urlencode(my_value)
    print(my_data)
    my_url += my_data
    req = request.Request(my_url, headers=my_header)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print('Error occured during web request!!!')
    print(sys.exc_info()[1])