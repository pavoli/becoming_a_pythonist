# coding: utf-8

__author__ = 'polly'

import random


'''
- реализовать на классах модель Карты
- 52 карты по значимости и 4 масти
- действие "добрать руку", "сходить"
- концепция "козырь"
'''


class Deck():
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit = ['♥', '♦', '♣', '♠']
    deck = []
    gameTable = []

    def __init__(self):
        self.CreateDeck()

    #здесь создается игровая колода из 52 карт
    #затем колода тасуется
    def CreateDeck(self):
        self.deck = [card + color for card in self.rank for color in self.suit]
        random.shuffle(self.deck)

        print ''
        self.PrintDeck()

    #выводит на печать текущую колоду карт
    def PrintDeck(self):
        print 'Deck has these cards:'
        for item in self.deck:
            print item,
        print ' (%d)' % len(self.deck)

    def deckAfterGiving(self):
        print 'new deck after giving cards to players: %d' % len(self.deck)
        print ''

    #создаем козырь
    def CreateTrump(self):
        trump = self.deck[-1]
        self.deck.remove(trump)
        self.deck.insert(0, trump)
        print ''
        print 'trump is %s' % trump[-3:]
        self.trump = trump


class Player():
    name = ''
    cards = []

    def __init__(self, name):
        self.CreatePlayer(name, deck)

    #создаем игрока
    #присваиваем ему имя
    #записываем в словарь с игроком
    def CreatePlayer(self, name, deck):
        playerDeck = []

        print ''
        for i in range(0, 6):
            playerDeck += [deck.deck.pop()]
        newDeck = playerDeck
        self.name = name
        self.cards = newDeck

    # выводит на печать карты игрока
    def PlayerHas(self):
        print '%s has:' % self.name
        for item in self.cards:
            print item,
        print ''

    def Move(self):
        pass


deck = Deck()
tom = Player('Tom')
alex = Player('Alex')
tom.PlayerHas()
alex.PlayerHas()
deck.PrintDeck()
deck.CreateTrump()
