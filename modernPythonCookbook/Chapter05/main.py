#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

from pathlib import Path
import csv
from collections import OrderedDict
import sys


print("Chapter05")

count = 333
print("count is", count)


def get_fuel_use(source_path):
    with source_path.open() as source_file:
        rdr = csv.DictReader(source_file)
        od = (OrderedDict(
            [(column, row[column]) for column in rdr.fieldnames]) for row in rdr)
        data = list(od)
    return data


source_path = Path("./test.csv")
fuel_use = get_fuel_use(source_path)

print(fuel_use)


'''

this did not work from book 

for leg in fuel_use:
    start = float(leg['fuel height on'])
    finish = float(leg['fuel height off'])
    print("On ", leg['date'],
          "from ", leg['engine on'],
          "to ", leg['engine off'],
          "change ", start-finish, "in")
    
'''

print("Red Alert!", file=sys.stderr)







