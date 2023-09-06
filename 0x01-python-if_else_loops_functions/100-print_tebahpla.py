#!/usr/bin/python3
z = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - z)), end="")
    z = 32 if z == 0 else 0
