#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv_num = len(sys.argv)
print("{} arguments".format(argv_num - 1), end="")
if argv_num == 1:
    print(".")
else:
    print(":")
    for i in range(1, argv_num):
        print("{}: {}".format(i, sys.argv[i]))
