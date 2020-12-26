import numpy as np
import itertools

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + " " + self.suit

class Hand:
    def __init__(self, first, second, third, fourth, fifth):
        self.cards = [first, second, third, fourth, fifth]
        self.values = [first.value, second.value, third.value, fourth.value, fifth.value]
        self.suit = [first.suit, second.suit, third.suit, fourth.suit, fifth.suit]

    def checkPair(self):
        pair = []
        others = []
        for i in self.values:
            if self.values.count(i) == 2:
                pair.append(i)
            elif self.values.count(i) == 1:
                others.append(i)
                others.sort()
        score = 15 
        return score

    def checkTwoPair(self):
        pairs = []
        others = []
        for i in self.values:
            if self.values.count(i) == 2:
                pairs.append(i)
            elif self.values.count(i) == 1:
                others.append(i)
                others.sort()
        score = 30

    def scoreHand(self):
        pass

    def __str__(self):
        return (f'{self.first}, {self.second}, {self.third}, {self.fourth}, {self.fifth}')

class Deck:
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.handsArr = []
        self.generateCombinations()
        self.convertToHands()

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

    def convertToHands(self):
        index = 0
        for i in self.handsArr:
            self.handsArr[index] = Hand(i[0], i[1], i[2], i[3], i[4])
            index += 1

    def printDeck(self):
        for i in self.deck:
            print(i)

    def printHands(self):
        for i in self.handsArr:
            print(i)

    #def shuffle(self):

deck = Deck()
deck.printDeck()

