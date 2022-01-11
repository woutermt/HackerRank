#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    res_list = []

    for i in range(len(arr)):
        res_list.append(sum(arr) - arr[i])

    print(min(res_list), max(res_list))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
