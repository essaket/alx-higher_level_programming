#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    m = my_list[0]
    for i in range(len(my_list)):
        m = my_list[i] if my_list[i] > m
    return (m)
