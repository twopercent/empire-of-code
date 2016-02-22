#!/bin/env python3

def most_difference(*args):
    values = () 
    print(len(args))
    print(len(values))
    
    for value in args:
        values += value
    

    print(len(values))
    
    if len(values) == 0:
        return 0

    else:
        diff = max(values) - min(values)
        return round(diff, 3)

#print('diff = ' + str(max(values) - min(values)))

testa = (1, 2.2, 3.2)
testb = (3, 8, 10.2, 0.00001, 1.1)
testc = (10.2, -2.2, 0, 1.1, 0.5)

print(most_difference(testa))
print(most_difference(testb))
print(most_difference(testc))



