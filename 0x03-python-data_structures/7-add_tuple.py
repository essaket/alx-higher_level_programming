#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = tuple_a[0] if len(tuple_a) >= 1 else 0
    j = tuple_a[1] if len(tuple_a) >= 2 else 0
    k = tuple_b[0] if len(tuple_b) >= 1 else 0
    l = tuple_b[1] if len(tuple_b) >= 2 else 0
    return (i + k, j + l)
