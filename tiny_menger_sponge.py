#!/usr/bin/env python3

sponge = [[True]]
for i in range(int(input())):
    sponge = [[False if x == y == 1 else c for c in r for y in range(3)] for r in sponge for x in range(3)]
print("\n".join("".join(("\u2588" if c else " ") * 2 for c in r) for r in sponge))
