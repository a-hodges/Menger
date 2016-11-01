#!/usr/bin/env python3

sponge = ['\u2588\u2588']

for i in range(int(input())):
    new = []
    for x in range(3):
        for r in sponge:
            newline = []
            for y in range(3):
                for col in r:
                    if x == 1 and y == 1:
                        newline.append('  ')
                    else:
                        newline.append(col)
            new.append(newline)
    sponge = new
        
for r in sponge:
    for c in r:
        print(c, end='')
    print()
