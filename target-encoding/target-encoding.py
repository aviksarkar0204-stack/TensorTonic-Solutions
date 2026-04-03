def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    result = {}
    for c,t in zip(categories,targets):
        if c not in result:
            result[c] = {"sums":0,"counts":0}
        result[c]["sums"] += t
        result[c]["counts"] += 1
    mean = {}
    for c in result:
        mean[c] = result[c]["sums"]/result[c]["counts"]
    return [mean[c] for c in categories]