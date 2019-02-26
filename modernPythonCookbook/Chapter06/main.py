#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

print("Chapter06")

import random
random.seed(1)

from dice import Dice
from player import Player
from hand import Hand
from counterstatistics import CounterStatistics
from collections import Counter

from fractions import Fraction

from collections import namedtuple

d1 = Dice()

d1.roll()
print(d1.total())
print(d1.faces)
print(d1.hardway())

def arrival1(n=8):
    while True:
        yield random.randrange(n)

def expected(n=8):
    return n * sum(Fraction(1, (i+1)) for i in range(n))

def coupon_collector(n, data):
           count, collection = 0, set()
           for item in data:
               count += 1
               collection.add(item)
               if len(collection) == n:
                   yield count
                   count, collection = 0, set()

def samples(limit, generator):
    for n, value in enumerate(generator):
        if n == limit: break
        yield value

def raw_data(n=8, limit=1000, arrival_function=arrival1):
    expected_time = float(expected(n))
    data = samples(limit, arrival_function(n))
    wait_times = Counter(coupon_collector(n, data))
    return wait_times


data = raw_data()
stats = CounterStatistics(data)

print("mean: {0:.2f}".format(stats.mean))
print("Standard Deviation: {0:.3f}".format(stats.stddev))

p = Player()
p.stake = 100

print(p.stake)

Card = namedtuple('Card', ('rank', 'suit'))

h1 = Hand(2)
h1.deal(Card(rank=4, suit='\N{White Heart Suit}'))
h1.deal(Card(rank=8, suit='\N{White Spade Suit}'))

print(h1)
