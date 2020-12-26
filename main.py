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
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.values = [int(first.value), int(second.value), int(third.value), int(fourth.value), int(fifth.value)]
        self.values = sorted(self.values, reverse=True)
        self.suits = [first.suit, second.suit, third.suit, fourth.suit, fifth.suit]
        self.sameSuits = [self.suits.count(suit) for suit in self.suits]
        self.sameNums = [self.values.count(value) for value in self.values]
        self.isStraight = (self.values[0] - self.values[4] == 4)
        self.isFlush = (self.sameSuits[0] == 5)
        self.handType = None
        #self.score = -1

    def checkPair(self):
        if (self.sameNums.count(2) != 2):
            return False
        #pair = -1
        #others = []
        #for i in self.values:
        #    if self.values.count(i) == 2:
        #        pair = 1
        #    else:
        #        others.append(i)
        #        others.sort()
        return True

    def checkTwoPair(self):
        if (self.sameNums.count(2) != 4):
            return False
        #pairs = []
        #others = []
        #for i in self.values:
        #    if self.values.count(i) == 2:
        #        pairs.append(i)
        #        pairs.sort()
        #    else:
        #        others.append(i)
        return True

    def checkThreeOfKind(self):
        if (self.sameNums.count(3) != 3):
            return False
        #three = -1
        #others = []
        #for i in self.values:
        #    if self.values.count(i) == 3:
        #        three = i
        #    else:
        #        others.append(i)
        #        others.sort()
        return True

    def checkStraight(self):
        return self.isStraight

    def checkFlush(self):
        return self.isFlush

    def checkFullHouse(self):
        if (self.sameNums.count(3) != 3 or self.sameNums.count(2) != 2):
            return False
        #three = -1
        #two = -1
        #for i in self.values:
        #    if self.values.count(i) == 3:
        #        three = i
        #    elif self.values.count(i) == 2:
        #        two = i
        return True

    def checkFourOfKind(self):
        if (self.sameNums.count(4) != 4):
            return False
        #four = -1
        #other = -1
        #for i in self.values:
            #if self.values.count(i) == 4:
            #    four = i
            #elif self.values.count(i) == 1:
            #    other = i
        return True

    def checkStraightFlush(self):
        if (self.isStraight == False or self.isFlush == False):
            return False
        return True

    def checkRoyalFlush(self):
        if (self.isFlush == False or self.values != [14, 13, 12, 11, 10]):
            return False
        return True

    def decideHand(self):
        if self.checkRoyalFlush():
            self.handType = "Royal Flush"
            return
        if self.checkStraightFlush():
            self.handType = "Straight Flush"
            return
        if self.checkFourOfKind():
            self.handType = "Four of a Kind"
            return
        if self.checkFullHouse():
            self.handType = "Full House"
            return
        if self.checkFlush():
            self.handType = "Flush"
            return
        if self.checkStraight():
            self.handType = "Straight"
            return
        if self.checkThreeOfKind():
            self.handType = "Three of a kind"
            return
        if self.checkTwoPair():
            self.handType = "Two pair"
            return
        if self.checkPair():
            self.handType = "Pair"
            return
        self.handType = "High card"
        return

    def __str__(self):
        self.decideHand()
        return (f'{self.first}, {self.second}, {self.third}, {self.fourth}, {self.fifth}: {self.handType}')

class Deck:
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.handsArr = []

    def createDeck(self):
        suits = ["spades", "clubes", "diamonds", "hearts"]
        numbers = []
        self.deck = []
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
deck.generateCombinations()
deck.convertToHands()
deck.printHands()

