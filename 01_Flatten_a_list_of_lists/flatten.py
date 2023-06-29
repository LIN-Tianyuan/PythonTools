"""
Flatten data into a one-dimensional list

matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5]
]

->

[9, 3, 8, 3, 4, 5, 2, 8, 6, 4, 3, 1, 1, 0, 4, 5]
"""

from itertools import chain
from functools import reduce

my_matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5]
]


def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list


def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]


def flatten_chain(matrix):
    return list(chain.from_iterable(matrix))


def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))


def flatten_sum(matrix):
    return sum(matrix, [])


print(flatten_extend(my_matrix))
print(flatten_comprehension(my_matrix))
print(flatten_chain(my_matrix))
print(flatten_reduce_lambda(my_matrix))
print(flatten_sum(my_matrix))