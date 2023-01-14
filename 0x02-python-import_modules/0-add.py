#!/usr/bin/python3
from add_0 import add
"""Print the sum of 1 and 2."""


def sum():
    a = 1
    b = 2
    add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))


if __name__ == "__main__":
    sum()
