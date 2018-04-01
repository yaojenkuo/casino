# coding=utf-8
from random import choice

def roll_dice():
    '投擲骰子'
    dice = range(1, 7)
    return choice(dice)
