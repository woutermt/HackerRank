#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(n, c):
    skip = False
    jump = 0
    i = 0

    while i + 1 < n:

        if c[i + 1] == 1 or skip == False:
            skip = True
            i += 1
            jump += 1

        else:
            skip = False
            i += 1

    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
