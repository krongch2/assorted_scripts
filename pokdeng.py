import numpy as np
import pandas as pd

suits = ['♠', '♦', '♥', '♣']
kinds = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def str2card(s):
    kind = s[:-1]
    suit = s[-1]
    return {
        'kind': kind,
        'suit': suit,
        'value': card_value(kind)
    }
def handstr2handdict(l):
    return [str2card(card) for card in l]

def card_value(kind):
    if kind == 'A':
        value = 1
    elif kind in ['J', 'Q', 'K']:
        value = 10
    else:
        value = int(kind)
    return value

def hand_value(hand):
    return sum(card['value'] for card in hand) % 10

def hand_rank(hand):
    face_kinds = ['J', 'Q', 'K']
    if len(hand) == 2 and hand_value(hand) in [8, 9]:
        return 'pok'
    elif len(hand) == 3 and (hand[0]['kind'] == hand[1]['kind'] == hand[2]['kind']):
        return 'tong'
    elif len(hand) == 3 and (hand[0]['kind'] in face_kinds and hand[1]['kind'] in face_kinds and hand[2]['kind'] in face_kinds):
        return 'face'
    else:
        return 'normal'

def hand_deng(hand):
    if hand_rank(hand) == 'tong':
        return 5
    elif hand_rank(hand) == 'face':
        return 3
    else:
        if len(hand) == 2 and (hand[0]['kind'] == hand[1]['kind'] or hand[0]['suit'] == hand[1]['suit']):
            return 2
        elif len(hand) == 3 and (hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']):
            return 3
        else:
            return 1

def compare_hands(hand1, hand2):
    # todo
    pass

cards = [{'kind': kind, 'suit': suit, 'value': card_value(kind)} for kind in kinds for suit in suits]
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

d = pd.DataFrame({'hand_str': test_hands})
d['hand_dict'] = d['hand_str'].apply(handstr2handdict)
d['hand_rank'] = d['hand_dict'].apply(hand_rank)
d['hand_value'] = d['hand_dict'].apply(hand_value)
d['hand_deng'] = d['hand_dict'].apply(hand_deng)
print(d)


# print([[str2card(card) for card in hand] for hand in test_hands])

