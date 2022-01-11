#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    # n = int(input())

    count = [0, 0, 0]
    for i in range(n):
        if arr[i] > 0:
            count[0] += 1
        if arr[i] < 0:
            count[1] += 1
        if arr[i] == 0:
            count[2] += 1

    print(count[0] / n)
    print(count[1] / n)
    print(count[2] / n)

    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
