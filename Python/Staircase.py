#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    row = 1

    for i in range(n):
        s = ''
        for j in range(n):
            if j < n - row:
                s += ' '

            else:
                s += '#'

        row += 1
        print(s)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
