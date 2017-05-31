#!/usr/bin/env python3

r = range(3 ** ~-int(input()))

for i in r:
    for j in r:
        l = [(i // (3**k) % 3, j // (3**k) % 3) for k in r]
        c = "# "[any(x == y == 1 for x, y in l)]
        # print(i, j, c, l)
        print(c, end=" ")
    print()
