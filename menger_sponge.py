#!/usr/bin/env python3

import bpy

class Sponge (object):
    p = True  # positive space
    n = False # negative space

    def __init__(self, size=0, dimension=2):
        r"""
        Creates a new sponge
        Sponges should not change dimension after creation
        """
        self._dimension = dimension
        self.size = size

    def _iterate(self, block, d, middle=0):
        r"""
        Recursively iterates sponge
        """
        if d <= 0:
            new = block and middle < (self._dimension - 1)
        else:
            new = []
            for x in range(3):
                if x == 1:
                    m = middle + 1
                else:
                    m = middle
                for line in block:
                    new.append(self._iterate(line, d-1, m))
        return new

    @property
    def dimension(self):
        return self._dimension

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        r"""
        Resizes the sponge
        The size must be >= 0
        """
        if size < 0:
            raise ValueError("Size must be >= 0")
        elif not hasattr(self, "_size") or size < self._size:
            self._size = 0
            self._sponge = True
            for _ in range(self.dimension):
                self._sponge = [self._sponge]
            for _ in range(size):
                self._sponge = self._iterate(self._sponge, self.dimension)
                self._size += 1
        elif size > self._size:
            for _ in range(self._size, size):
                self._sponge = self._iterate(self._sponge, self.dimension)
                self._size += 1

    @property
    def space(self):
        return (3 ** self.size) ** self.dimension

    @property
    def area(self):
        r"""
        Not working
        """
        volume = {
            0: 1,
            1: 2,
            2: 8,
            3: 20,
        }.get(self.dimension, 8)
        return volume ** self.size

    def _get_strs(self, l):
        r"""
        Recursively obtain lists of strings
        """
        if isinstance(l, bool):
            new = self.p if l else self.n
        elif isinstance(l, list):
            new = []
            for item in l:
                new.append(self._get_strs(item))
        else:
            raise TypeError("Found item, not boolen or list")
        return new

    def __str__(self):
        def symbol(bool):
            return "\u2588"*2 if bool else "  "
        lines = self._sponge
        for _ in reversed(range(2, self.dimension)):
            lines = lines[len(lines) // 2]
        ret = self._get_strs(lines)
        if self.dimension >= 2:
            ret = "\n".join(map("".join, map(symbol, ret)))
        elif self.dimension == 1:
            ret = "".join(ret)
        return ret

    def __iter__(self):
        return iter(self._sponge)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Menger Sponge Generator")
    parser.add_argument("size", type=int, help="The number of iterations to perform")
    parser.add_argument("-p", "--parameters", action="store_true", help="Print the sponge's attributes")
    parser.add_argument("-d", "--dimension", default=2, type=int, help="The number of dimensions for the parameters")

    args = parser.parse_args()

    s = Sponge(args.size, args.dimension)
    if args.parameters:
        print("Size: %d" % s.space)
        print("Area: %d" % s.area)
    print(s)
