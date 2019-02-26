#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

class Hand:
    __slots__ = ('hand', 'bet')

    def __init__(self, bet, hand=None):
        self.hand = hand or []
        self.bet = bet

    def deal(self, card):
        self.hand.append(card)


    def __repr__(self):
        return "{class_}({bet}, {hand})".format(
        class_= self.__class__.__name__,
        **vars(self)
        )
