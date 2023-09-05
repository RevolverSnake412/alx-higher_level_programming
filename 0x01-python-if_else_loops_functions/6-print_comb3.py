#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}".format(i) + "{}".format(j), end="")
        if i == 8:
            print()
        else:
            print(", ", end="")
