# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


import json
filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': 'Hillary Clinton',
    'Score': 346,
    'awards': ['WI', 'IX', 'MI']
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# -------------- SAVE by JSON --------------

json.dump(myplayers, myfile)
myfile.close()

# -------------- LOAD by JSON --------------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)


for user in json_data:
    print('Player Name is {}'.format(user['PlayerName']))
    print('Player Score is {}'.format(user['Score']))
    print('Player Award #1: {}'.format(user['awards'][0]))
    print('Player Award #2: {}'.format(user['awards'][1]))
    print('Player Award #3: {}'.format(user['awards'][2]))