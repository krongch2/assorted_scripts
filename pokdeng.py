import numpy as np
import pandas as pd
import random

suits = ['♣', '♦', '♥', '♠']
kinds = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
face_kinds = ['J', 'Q', 'K']

class Card():

    def __init__(self, name):
        kind = name[:-1]
        suit = name[-1]
        self.name = name
        self.kind = kind
        self.suit = suit
        self.value = self.card_value()

    def card_value(self):
        if self.kind == 'A':
            value = 1
        elif self.kind in face_kinds:
            value = 10
        else:
            value = int(self.kind)
        return value

    def __str__(self):
        return self.name

class Hand():

    def __init__(self, names):
        self.cards = [Card(name) for name in names]
        self.names = names
        self.n = len(names)
        self.value = self.hand_value()
        self.rank = self.hand_rank()
        self.rank_order = self.hand_rank_order()
        self.deng = self.hand_deng()

    def hand_value(self):
        return sum(card.value for card in self.cards) % 10

    def hand_rank(self):
        if self.n == 2 and self.value in [8, 9]:
            return 'pok'
        elif self.n == 3 and (self.cards[0].kind == self.cards[1].kind == self.cards[2].kind):
            return 'tong'
        elif self.n == 3 and (self.cards[0].kind in face_kinds and self.cards[1].kind in face_kinds and self.cards[2].kind in face_kinds):
            return 'face'
        else:
            return 'normal'

    def hand_rank_order(self):
        rank_order = ['normal', 'face', 'tong', 'pok']
        return rank_order.index(self.rank)

    def hand_deng(self):
        if self.rank == 'tong':
            return 5
        elif self.rank == 'face':
            return 3
        else:
            if self.n == 2 and (self.cards[0].kind == self.cards[1].kind or self.cards[0].suit == self.cards[1].suit):
                return 2
            elif self.n == 3 and (self.cards[0].suit == self.cards[1].suit == self.cards[2].suit):
                return 3
            else:
                return 1

    def draw(self, name):
        self.cards.append(Card(name))
        self.names.append(name)
        self.n += 1
        self.value = self.hand_value()
        self.rank = self.hand_rank()
        self.rank_order = self.hand_rank_order()
        self.deng = self.hand_deng()

    def __str__(self):
        return f'[{" ".join(self.names):<11}], Rank: {self.rank:>6}, Value: {self.value}, Deng: {self.deng}'

def compare(hand1, hand2):
    if hand1.rank_order > hand2.rank_order:
        return hand1.deng
    elif hand1.rank_order < hand2.rank_order:
        return -hand2.deng
    else:
        if hand1.value > hand2.value:
            return hand1.deng
        elif hand1.value < hand2.value:
            return -hand2.deng
        else:
            if hand1.deng > hand2.deng:
                return hand1.deng - hand2.deng
            elif hand1.deng < hand2.deng:
                return -(hand2.deng - hand1.deng)
            else:
                return 0

def round(deck, nplayers):
    cutoff_value = 4
    chunks = [deck[i:i+2] for i in range(0, len(deck), 2)]
    hands = [Hand(chunk) for chunk in chunks[:nplayers]]
    topdeck_i = 2 * nplayers
    result = []
    for hand in hands:
        if hand.value <= cutoff_value:
            hand.draw(deck[topdeck_i])
            topdeck_i += 1
        result.append(compare(hand, hands[0]))
        # print(hand, compare(hand, hands[0]))
    result[0] = -sum(result[1:])
    return result

def sim(nrounds, nplayers):
    deck = [f'{kind}{suit}' for kind in kinds for suit in suits]
    results = []
    for _ in range(nrounds):
        results.append(round(random.sample(deck, len(deck)), nplayers))
    net = [sum(i) for i in zip(*results)]
    print(net)
    return net

sim(10000, 10)
