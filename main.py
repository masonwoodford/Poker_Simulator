import numpy as np
import itertools


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        #self.img = ...

    def __str__(self):
        return self.value + " " + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.handsArr = []
        self.generateCombinations()

    def createDeck(self):
        suits = ["spades", "clubes", "diamonds", "hearts"]
        numbers = []
        deck = []
        for i in range(2, 15):
            numbers.append(str(i))
        for suit in suits:
            for value in numbers:
                self.deck.append(Card(value, suit))

    def generateCombinations(self):
        self.handsArr = itertools.combinations(self.deck, 5)
        self.handsArr = list(self.handsArr)


    def printDeck(self):
        for i in self.deck:
            print(i)

    #def printHands(self):
    #    for i in self.handsArr:
    #        print(i[0], i[1], i[2], i[3], i[4])


    #def shuffle(self):

deck = Deck()
deck.printDeck()
#deck.printHands()

