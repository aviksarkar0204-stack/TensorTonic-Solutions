import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    vector_x = np.array(x)
    vector_y = np.array(y)
    vector_diff = vector_x - vector_y
    vector_squared = vector_diff ** 2

    distance = np.sqrt(np.sum(vector_squared))

    return distance

    