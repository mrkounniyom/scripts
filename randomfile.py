#!/usr/bin/env python3

import os, random

direc = input('enter path: ')

if direc != '':
    os.chdir(direc)
    files = os.listdir('.')
    print(len(files))
    rand = random.randrange(0, len(files))
    count = 0
    for item in files:
        if count == rand:
            print(item)
        count += 1
