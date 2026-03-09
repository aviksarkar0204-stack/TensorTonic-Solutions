import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x_vector = np.array(x)
    x_vector_mean = float(np.mean(x_vector))
    x_vector_median = float(np.median(x_vector))
    x_vector_mode = float(Counter(x_vector).most_common(1)[0][0])
    
    return x_vector_mean, x_vector_median, x_vector_mode

x = [1,2,3,4]
mean_median_mode(x)