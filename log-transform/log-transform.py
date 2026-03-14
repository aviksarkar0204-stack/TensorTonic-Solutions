def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    array = np.array(values)
    log_trans = np.log1p(array)
    return log_trans


