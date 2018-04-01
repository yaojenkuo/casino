# coding=utf-8
from random import choice


def roll_a_dice():
    """
    Roll a dice
    """
    dice = range(1, 7)
    return choice(dice)
