import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    return 1/(1 + np.exp(-x))

values = np.array([0,2,-2])
print(sigmoid(values))