import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    return np.transpose(A)

    # r = len(A)
    # c = len(A[0])
    # res = [[0] * r for _ in range(c)]
    # for i in range(r):
    #     for j in range(c):
    #         res[j][i] = A[i][j]
    # return res
    
