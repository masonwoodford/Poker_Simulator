import operator
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
        self.decideHand()

    def checkPair(self):
        if (self.sameNums.count(2) != 2):
            return False
        pair = -1
        others = []
        for i in self.values:
            if self.values.count(i) == 2:
                pair = 1
            else:
                others.append(i)
                others.sort()
        self.score = pair + others[0]/10000 + others[1]/1000 + others[2]/100
        return True

    def checkTwoPair(self):
        if (self.sameNums.count(2) != 4):
            return False
        pairs = []
        others = []
        for i in self.values:
            if self.values.count(i) == 2:
                pairs.append(i)
            else:
                others.append(i)
        pairs.sort()
        self.score = pairs[0]/1000 + pairs[1]/100 + others[0]/10000
        return True

    def checkThreeOfKind(self):
        if (self.sameNums.count(3) != 3):
            return False
        three = -1
        others = []
        for i in self.values:
            if self.values.count(i) == 3:
                three = i
            else:
                others.append(i)
        others.sort()
        self.score = three + others[0]/1000 + others[1]/100
        return True

    def checkStraight(self):
        self.score = self.values[0]
        return self.isStraight

    def checkFlush(self):
        self.score = self.values[0]
        return self.isFlush

    def checkFullHouse(self):
        if (self.sameNums.count(3) != 3 or self.sameNums.count(2) != 2):
            return False
        three = -1
        two = -1
        for i in self.values:
            if self.values.count(i) == 3:
                three = i
            elif self.values.count(i) == 2:
                two = i
        self.score = two/1000 + three/100
        return True

    def checkFourOfKind(self):
        if (self.sameNums.count(4) != 4):
            return False
        four = -1
        other = -1
        for i in self.values:
            if self.values.count(i) == 4:
                four = i
            elif self.values.count(i) == 1:
                other = i
        self.score = four/100 + other/1000
        return True

    def checkStraightFlush(self):
        if (self.isStraight == False or self.isFlush == False):
            return False
        self.score = self.values[0]
        return True

    def checkRoyalFlush(self):
        if (self.isFlush == False or self.values != [14, 13, 12, 11, 10]):
            return False
        self.score = float('inf')
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
        return (f'{self.first}, {self.second}, {self.third}, {self.fourth}, {self.fifth}: {self.handType}')

class Deck:
    def __init__(self):
        self.deck = []
        self.createDeck()

        self.handsArr = []

        self.royalFlushes = []
        self.straightFlushes = []
        self.fourOfAKinds = []
        self.fullHouses = []
        self.flushes = []
        self.straights = []
        self.threeOfAKinds = []
        self.twoPairs = []
        self.pairs = []
        self.highCardHands = []

        self.isConverted = False
        self.isSorted = False

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
        assert(self.isConverted == False), "Conversion being called twice"
        self.isConverted = True
        for i in self.handsArr:
            temp = Hand(i[0], i[1], i[2], i[3], i[4])
            if temp.handType == "Royal Flush":
                self.royalFlushes.append(temp)
            elif temp.handType == "Straight Flush":
                self.straightFlushes.append(temp)
            elif temp.handType == "Four of a kind":
                self.fourOfAKinds.append(temp)
            elif temp.handType == "Full House":
                self.fullHouses.append(temp)
            elif temp.handType == "Flushes":
                self.flushes.append(temp)
            elif temp.handType == "Straights":
                self.straights.append(temp)
            elif temp.handType == "Three of a kind":
                self.threeOfAKinds.append(temp)
            elif temp.handType == "Two Pair":
                self.twoPairs.append(temp)
            elif temp.handType == "Pair":
                self.pairs.append(temp)
            else:
                self.highCardHands.append(temp)

    def sortHands(self):
        assert(self.isSorted == False), "Hands sorting method being called twice"
        self.royalFlushes.sort(key=operator.attrgetter('score'))
        self.straightFlushes.sort(key=operator.attrgetter('score'))
        self.fourOfAKinds.sort(key=operator.attrgetter('score'))
        self.fullHouses.sort(key=operator.attrgetter('score'))
        self.flushes.sort(key=operator.attrgetter('score'))
        self.straights.sort(key=operator.attrgetter('score'))
        self.threeOfAKinds.sort(key=operator.attrgetter('score'))
        self.twoPairs.sort(key=operator.attrgetter('score'))
        self.pairs.sort(key=operator.attrgetter('score'))
        self.highCardHands.sort(key=operator.attrgetter('score'))
        self.isSorted = True

    def printDeck(self):
        for i in self.deck:
            print(i)

    def printHands(self):
        if self.isConverted == False:
            self.convertToHands()
        for i in self.handsArr:
            print(i)

    def printRoyalFlushes(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.royalFlushes:
            print(i)

    def printStraightFlushes(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.straightFlushes:
            print(i)

    def printFourOfAKinds(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.fourOfAKinds:
            print(i)

    def printFullHouses(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.fullHouses:
            print(i)

    def printFlushes(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.flushes:
            print(i)

    def printStraights(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.straights:
            print(i)

    def printThreeOfAKinds(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.threeOfAKinds:
            print(i)

    def printTwoPairs(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.twoPairs:
            print(i)

    def printPairs(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.pairs:
            print(i)

    def printHighCards(self):
        if self.isConverted == False:
            self.convertToHands()
        if self.isSorted == False:
            self.sortHands()
        for i in self.highCardHands:
            print(i)

deck = Deck()
deck.generateCombinations()
deck.printTwoPairs()

