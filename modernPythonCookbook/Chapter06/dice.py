#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
dice class
'''
import random
random.seed(1)

class Dice:
    def __init__(self):
        self.faces = None

    def roll(self):
        self.faces = (random.randint(1,6), random.randint(1,6))

    def total(self):
        return sum(self.faces)

    def hardway(self):
        return self.faces[0] == self.faces[1]
    def easyway(self):
        return self.faces[0] != self.faces[1]
