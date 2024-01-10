#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a, b = 0, 0
    for x in my_list:
        a += x[0] * x[1]
        b += x[1]
    return (a / b)
