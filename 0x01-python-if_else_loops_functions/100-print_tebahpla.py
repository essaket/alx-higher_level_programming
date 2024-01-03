#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    y = 0 if x % 2 == 0 else y = 32
    print("{}".format(x - y), end="")
