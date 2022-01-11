#!/bin/python3

import math
import os
import random
import re
import sys


def hourglasses(arr):
    n = len(arr[0])
    hg_sum = []

    for x in range(0, n - 2):
        for y in range(0, n - 2):
            hg_sum.append(sum(arr[x][y:y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y:y + 3]))

    print(max(hg_sum))


if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglasses(arr)



