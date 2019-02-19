#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

from collections import namedtuple

Card = namedtuple('Card', ('rank', 'suit'))
eight_hearts = Card(rank=8, suit='\N{White Heart Suit}')

print(eight_hearts)
print(eight_hearts.rank)
print(eight_hearts.suit)
print(eight_hearts[0])
