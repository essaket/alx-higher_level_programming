#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Sum = 0
    for x in range(len(sys.argv) - 1):
        Sum += int(sys.argv[i + 1])
    print("{}".format(Sum))