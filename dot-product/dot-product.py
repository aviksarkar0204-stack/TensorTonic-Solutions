import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x_vector = np.array(x)
    y_vector = np.array(y)
    return np.dot(x_vector,y_vector)

x = np.array([1,2,3])
y = np.array([4,5,6])

dot_product(x,y)