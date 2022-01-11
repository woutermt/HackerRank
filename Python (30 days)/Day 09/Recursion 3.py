#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    num = n
    res = 1

    while num != 0:
        res = res * num
        num -= 1

    return res
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
