#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

import math


print("Chapter 02")
print("Hello World")
print(355/113)

example_value = (63/25) * (17+15*math.sqrt(5)) / (7+15*math.sqrt(5))
mantissa_fraction, exponent = math.frexp(example_value)
mantissa_whole = int(mantissa_fraction*2**53)
message_text = 'the internal representation is {mantissa:d}/2**53*2**{exponent:d}'.format(mantissa=mantissa_whole, exponent=exponent)
print(message_text)

