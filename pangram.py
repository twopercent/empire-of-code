#!/bin/env python3

import string

def check_pangram(text):
    is_pangram = True
    print(text.lower())
    for letter in string.ascii_lowercase:
        if letter not in text.lower():
            print("no " + str(letter))
            is_pangram = False
    return is_pangram



check_pangram('this is a test sentence')
check_pangram('THE QUICK brown fox Jumps OVER the LAZY Dog')
