"""
Flattening Python Lists for Data Science With NumPy
"""
import numpy as np

matrix = np.array(
    [
        [9, 3, 8, 3],
        [4, 5, 2, 8],
        [6, 4, 3, 1],
        [1, 0, 4, 5],
    ]
)

print(matrix)
print(matrix.flatten())
"""
[[9 3 8 3]
 [4 5 2 8]
 [6 4 3 1]
 [1 0 4 5]]
 
[9 3 8 3 4 5 2 8 6 4 3 1 1 0 4 5]
"""