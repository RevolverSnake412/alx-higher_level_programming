#!/usr/bin/python3
'''function that finds the peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    size = len(list_of_integers)
    peak = 0

    if size == 0:
        return None

    for i in range(1, size - 1, 2):
        current = list_of_integers[i]
        prev = list_of_integers[i - 1]
        next = list_of_integers[i + 1]

        if size % 2 == 0 and i == size - 3:
            current = list_of_integers[i + 1]
            prev = list_of_integers[(i - 1) + 1]
            next = list_of_integers[(i + 1) + 1]

        if current >= prev and current >= next:
            if current > peak:
                peak = current

    return peak
