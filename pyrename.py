#!/usr/bin/python
import os, random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'z', 'y'
]
#enter the path to the folder: relative or absolute
direc = input('Enter the path to directory: ')
os.chdir(direc)
files = os.listdir('.')
for i,x in enumerate(files, 1):
    name, ext = os.path.splitext(x)
    count = 0
    newName = ""
    while count < 13:
        newName = newName + str(random.choice(letters))
        count += 1
    os.rename(x, '{}_{}{}'.format(i,newName, ext))
