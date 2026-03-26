import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    matrix_a = np.array(a)
    matrix_b = np.array(b)

    dot_product = np.dot(matrix_a , matrix_b)

    norm_a = np.linalg.norm(matrix_a)
    norm_b = np.linalg.norm(matrix_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)