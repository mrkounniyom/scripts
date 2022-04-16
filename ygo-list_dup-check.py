#!/usr/bin/env python3

f = open("/home/mk/Downloads/cardpool2.txt", "r")
n = open("/home/mk/Downloads/sortpool2.txt", "w")

array = []

for x in f:
    new = x[2:]
    array.append(new)

array.sort()

nodups = []

# remove dups
for i in range(0, len(array)):

    duplicate = True

    for j in range(i+1, len(array)):
        if(array[i] == array[j]):
            duplicate = False
            break
    if(duplicate):
        nodups.append(array[i])


for item in nodups:
    n.write(item)

f.close()
n.close()
