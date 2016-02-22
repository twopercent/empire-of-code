#!/bin/env python3

def convert(str_number, radix):
    index = len(str_number)
    result = 0

    for pos in str_number:
        index -= 1        
        
        # Assign the variable value with the digit or
        # a decimal representation of the letter         
        if pos.isdigit():
            value = int(pos)
        else:
            value = ord(pos) - 55

        # Check to see if the current position is greater
        # than the radix, return -1 if it is
        if value >= radix:
            print("char " + str(pos) + " is larger than radix " + str(radix)) 
            return -1

        
        # Add to the result the  value of the current position
        # multiplied by radix to the power of the index       
        result += value * radix**index

    return result

print(convert("101011", 2))
print(convert("AB", 10))
