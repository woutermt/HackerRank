#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # numSwaps
    n_swap = 0
    for i in range(n - 1):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a_n = a.pop(j)
                a.insert(j + 1, a_n)
                n_swap += 1

    print("Array is sorted in", n_swap, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
