import numpy as np
def transpose(matrix):
    return np.array(matrix).T.tolist()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))