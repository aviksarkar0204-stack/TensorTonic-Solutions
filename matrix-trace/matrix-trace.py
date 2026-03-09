import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A_matrix = np.array(A)
    return A_matrix.trace()

A = [[1,2],[3,4]]
matrix_trace(A)
