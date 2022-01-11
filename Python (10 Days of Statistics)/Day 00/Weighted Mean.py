#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY V
#  2. INTEGER_ARRAY W
#

def weightedMean(V, W):
    w_mean = 0.0
    w_vals = []

    for i in range(len(V)):
        w_vals.append(V[i] * W[i])

    w_mean = sum(w_vals) / sum(W)

    print(round(w_mean, 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
