#!/bin/python3

import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    max_val = 0

    for a in range(K - 2, N + 1):
        for b in range(a + 1, N + 1):
            if a & b < K and a & b > max_val:
                max_val = a & b

    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
