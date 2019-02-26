#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

import random
import warnings

print("Chapter03")

#random.seed(0)

def die(sides=6):
    return random.randint(1, sides)

def craps():
    return dice()

def zonk():
    return dice(6)

def dice(n=2, sides=6):
    if(n == 1):
        n = 2
    return tuple(die(sides) for x in range(n))

print(zonk())
print(dice())
print(dice(1))
print(dice(6))
print(dice(3, 8)) # 3, 8 sided dice


'''
single function that can solve a Rate-Time-Distance (RTD) calculation

distance = rate * time
rate = distance / time time = distance / rate
distance = rate * time
rate = distance / time 
time = distance / rate
'''

def rtd(distance=None, rate=None, time=None):
    if distance is None:
        distance = rate * time
    elif rate is None:
        rate = distance / time
    elif time is None:
        time = distance / rate
    else:
        warnings.warning("Nothing to solve for")
    return dict(distance=distance, rate=rate, time=time)

#print(rtd(distance=31.2, rate=6))


def rtd2(**keywords):
    #print(keywords)
    rate = keywords.get('rate', None)
    time = keywords.get('time', None)
    distance = keywords.get('distance', None)
    rtd(distance, rate, time)


#print(rtd2(rate=4, distance=3))




