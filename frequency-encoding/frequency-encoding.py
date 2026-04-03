def frequency_encoding(values):
    result = {}
    for value in values:
        if value not in result:
            result[value] = {"count": 0}
        result[value]["count"] += 1

    frequencys = {}
    for frequency in result:
        frequencys[frequency] = result[frequency]["count"] / len(values)

    return [frequencys[value] for value in values]