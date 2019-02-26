#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

import pathlib
import csv
from fractions import Fraction

print("Chapter04")

valid_inputs = {"yes", "y", "no", "n"}
answer = None
# while answer not in valid_inputs:
#     answer = input("Continue? [y, n] ").lower()

# dictionary
scheme = {"Crimson": (220, 14, 60),
          "DarkCyan": (0,139,139),
          "Yellow": (255, 255, 0)}

print(scheme['Crimson'])

current_dir = pathlib.Path(__file__).parent
current_file = pathlib.Path(__file__)

home = pathlib.Path(current_dir).parent
print(home)

for path in home.glob('*/index.rst'):
    print(path.stat().st_size, path.parent)


file_sizes = []

for path in home.glob('*/index.rst'):
    file_sizes.append(path.stat().st_size)

print(file_sizes)
print(sum(file_sizes))

csvLoc = './test.csv'

with pathlib.Path(csvLoc).open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)
print(log_rows)

'''
log_rows is a multidimensional array
log_rows = list(reader)[0][0] return hello
also
print(log_rows[0][0]) return hello
'''

head, tail = log_rows[:4], log_rows[4:]
print(head[0])
#print(tail[-1])

reverseList = head[0]
reverseList.reverse()
print(reverseList)


def expected(n=8):
    return n * sum(Fraction(1, (i+1)) for i in range(n))

print(expected())
print(round(expected()))













