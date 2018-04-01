# coding=utf-8
from random import choice

def card_deal():
    '發撲克牌'
    spades = []
    hearts = []
    diamonds = []
    clubs = []
    denominations = map(str, range(2, 11)) + ['J', 'Q', 'K', 'Ace']

    for i in range(len(denominations)):
        spades.append(denominations[i] + " Spade")
        hearts.append(denominations[i] + " Heart")
        diamonds.append(denominations[i] + " Diamond")
        clubs.append(denominations[i] + " Club")

    poker_cards = spades + hearts + diamonds + clubs
    return choice(poker_cards)
