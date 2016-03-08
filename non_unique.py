#!/bin/env python3

def non_unique(data):
    output = []
    for i in data:
        if isinstance(i, str):
            if data.count(i.upper()) > 1 or data.count(i.lower()) > 1:
                output.append(i)
        else:
            if data.count(i) > 1:
                output.append(i)
    print(output)
    return output

non_unique([1,2,3,4,1,2])
non_unique([1,2,'A',1,2,'A','a'])
non_unique([1,'c','A',1,2,'A','a'])
