#!/usr/bin/env python3

sponge = [[True]]

for i in range(int(input())):
    new = []
    for x in range(3):
        for r in sponge:
            if x % 3 == 1:
                newline = r + ([False] * len(r)) + r
            else:
                newline = r * 3
            new.append(newline)
    sponge = new

for r in sponge:
    for c in r:
        if c:
            print("\u2588" * 2, end='')
        else:
            print(" " * 2, end='')
    print()
