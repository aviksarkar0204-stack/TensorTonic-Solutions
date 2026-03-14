import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    
    array = np.array(data,dtype = float)
    array_min = np.min(array,axis = 0)
    array_max = np.max(array,axis = 0)
    denominator = array_max - array_min
    return np.where(denominator == 0, 0, (array - array_min)/ denominator).tolist()
        