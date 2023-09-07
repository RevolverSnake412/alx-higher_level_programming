#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argc = len(sys.argv)
S = 0
for i in range(1, argc):
    S += int(sys.argv[i])
print(S)
