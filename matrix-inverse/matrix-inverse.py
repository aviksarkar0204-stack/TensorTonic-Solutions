import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A_matrix = np.array(A)
    try:
        A_matrix_inv = np.linalg.inv(A_matrix)
        return A_matrix_inv
    except np.linalg.LinAlgError:
        return None

A = [[1,2],[3,4]]
matrix_inverse(A)
