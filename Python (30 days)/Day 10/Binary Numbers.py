#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    max_len = 0
    binar = bin(n).split('b')
    for i in binar[1].split('0'):
        if len(i) > max_len:
            max_len = len(i)
    print(max_len)
