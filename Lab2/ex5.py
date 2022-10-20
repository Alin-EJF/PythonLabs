import numpy as np

def replace(matrix):
     for i in range(len(matrix)):
         for j in range(len(matrix[i])):
             if i > j:
                 matrix[i][j] = 0
     return matrix

"""
arr = np.matrix([[1, 1, 4, 2],
                [4, 2, 1, 1],
                [2, 2, 1, 1],
                [3, 4, 5, 3]])  idk why no work
"""
arr= [[1,1,1], [2,2,2], [3,3,3]]


print(replace(arr))