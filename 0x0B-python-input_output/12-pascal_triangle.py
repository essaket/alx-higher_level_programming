#!/usr/bin/python3
"""Defines a text file insertion function"""


def pascal_triangle(n):
    """Method that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        new = [1]
        for i in range(len(tri) - 1):
            new.append(tri[i] + tri[i + 1])
        new.append(1)
        triangles.append(new)
    return triangles
