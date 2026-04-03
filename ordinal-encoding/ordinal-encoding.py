def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    mapping = {}
    for idx,value in enumerate(ordering):
        mapping[value] = idx
    return [mapping[value] for value in values]