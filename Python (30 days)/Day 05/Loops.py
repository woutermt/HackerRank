#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    multiples = 10
    for i in range(1, multiples + 1):
        print(str(n) + " x " + str(i) + " = " + str(n * i))

