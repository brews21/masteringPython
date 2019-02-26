#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
CounterStatistics class
'''
import math
from collections import Counter

class CounterStatistics:

    def __init__(self, raw_counter:Counter):
        self.raw_counter = raw_counter
        self.mean = self.compute_mean()
        self.stddev = self.compute_stddev()

    def compute_mean(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += value*frequency
            count += frequency
        return total/count

    def compute_stddev(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency*(value-self.mean)**2
            count += frequency
        return math.sqrt(total/(count-1))
