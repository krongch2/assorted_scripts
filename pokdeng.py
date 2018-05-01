import numpy as np
import pandas as pd
import random

suits = ['♠', '♦', '♥', '♣']
kinds = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

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
        elif self.kind in ['J', 'Q', 'K']:
            value = 10
        else:
            value = int(self.kind)
        return value

    def __str__(self):
        return self.name

class Hand():

    def __init__(self, name_list):
        cards = []
        names = []
        for name in name_list:
            c = Card(name)
            cards.append(c)
            names.append(c.name)
        self.cards = cards
        self.n = len(cards)
        self.names = names
        self.value = self.hand_value()
        self.rank = self.hand_rank()
        self.rank_order = self.hand_rank_order()
        self.deng = self.hand_deng()

    def hand_value(self):
        return sum(card.value for card in self.cards) % 10

    def hand_rank(self):
        face_kinds = ['J', 'Q', 'K']
        if self.n == 2 and self.value in [8, 9]:
            return 'pok'
        elif self.n == 3 and (self.cards[0].kind == self.cards[1].kind == self.cards[2].kind):
            return 'tong'
        elif self.n == 3 and (self.cards[0]['kind'] in face_kinds and self.cards[1]['kind'] in face_kinds and self.cards[2]['kind'] in face_kinds):
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
            if self.n == 2 and (self.cards[0]['kind'] == self.cards[1]['kind'] or self.cards[0]['suit'] == self.cards[1]['suit']):
                return 2
            elif self.n == 3 and (self.cards[0]['suit'] == self.cards[1]['suit'] == self.cards[2]['suit']):
                return 3
            else:
                return 1

    def __str__(self):
        return f'[{" ".join(self.names)}], Value: {self.value}, Rank: {self.rank}, Deng: {self.deng}'

h = Hand(['K♣', 'K♦', 'K♥'])
print(h)

# def str2card(s):
#     kind = s[:-1]
#     suit = s[-1]
#     return {
#         'kind': kind,
#         'suit': suit,
#         'value': card_value(kind)
#     }
# def c(l):
#     # convert hand string to hand dict
#     return [str2card(card) for card in l]

# def card2str(card):
#     return f'{card["kind"]}{card["suit"]}'

def compare_hands(hand1, hand2):
    if hand1.rank_order > hand2.rank_order:
        return 'Win', hand1.deng
    elif hand1.rank_order < hand2.rank_order:
        return 'Lose', hand2.deng
    else:
        if hand1.value > hand2.value:
            return 'Win', hand1.deng
        elif hand1.value < hand2.value:
            return 'Lose', hand2.deng
        else:
            if hand1.deng > hand2.deng:
                return 'Win', hand1.deng - hand2.deng
            elif hand1.deng < hand2.deng:
                return 'Lose', hand2.deng - hand1.deng
            else:
                return 'Tie', 0

# deck = [{'kind': kind, 'suit': suit, 'value': card_value(kind)} for kind in kinds for suit in suits]
test_hands = [
    ['J♦', '9♥'],
    ['9♠', '9♦'],
    ['7♠', '7♥', '7♣'],
    ['K♣', 'K♦', 'K♥'],
    ['Q♣', 'J♣', 'J♦'],
    ['J♠', 'Q♠', 'K♠'],
    ['A♣', '4♣'],
    ['5♥', '7♥', '7♠']
]

for test_hand in test_hands:
    print(Hand(test_hand))

# d = pd.DataFrame({'hand_str': test_hands})
# d['hand_dict'] = d['hand_str'].apply(c)
# d['hand_rank'] = d['hand_dict'].apply(hand_rank)
# d['hand_value'] = d['hand_dict'].apply(hand_value)
# d['hand_deng'] = d['hand_dict'].apply(hand_deng)
# print(d)

# print(compare_hands(c(['J♦', '9♥']), c(['9♠', '9♦'])))
# player1 = []
# player2 = []
# shuffled = random.sample(deck, len(deck))
# player1 = shuffled[0:2]
# player2 = shuffled[2:4]
# print(player1)
# print(player2)
# print(compare_hands(shuffled[0], shuffled[1]))
# for card in shuffled:
#     if len(player1) == 2 or len(player2) == 2:
#         break

#     print(card2str(card))