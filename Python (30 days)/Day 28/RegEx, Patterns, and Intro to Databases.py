#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    namelist = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if emailID[-10:] == '@gmail.com':
            namelist.append(firstName)

    for name in sorted(namelist):
        print(name)
