#! /usr/bin/env python3

a = 1

def myFunction(val):
    global a
    a = val
    print(a)
    return a


print(a)
myFunction(2)
print(a)
