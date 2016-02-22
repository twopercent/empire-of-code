#!/bin/env python3

def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    if operation == "disjunction":
        return x or y
    if operation == "implication":
        return y or not x
    if operation == "exclusive":
        return x ^ y
    if operation == "equivalence":
        return int(not x ^ y)

print(boolean(0,1,"conjunction"))
print(boolean(0,1,"disjunction"))
print(boolean(0,1,"implication"))
print(boolean(0,1,"exclusive"))
print(boolean(0,1,"equivalence"))
