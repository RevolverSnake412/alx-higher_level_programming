#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size1 = len(matrix)

    for i in range(size1):
        size2 = len(matrix[i])

        for j in range(size2):
            if j == size2 - 1:
                print("{}".format(matrix[i][j]))
            else:
                print("{}".format(matrix[i][j]), end=" ")
