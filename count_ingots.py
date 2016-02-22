#!/bin/env python3

def count_ingots(report):
    ingot_total = 0
    ingot_list = report.rsplit(sep=',')

    for ingot in ingot_list:
        nines = ord(ingot[0]) - 65
        print(nines)
        ingot_total += ((nines * 9) + int(ingot[1]))
        print(ingot_total)


count_ingots("A2,B1")
