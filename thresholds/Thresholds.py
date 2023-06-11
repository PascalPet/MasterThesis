def absolute_threshold(threshold, cosinusResults):
    result = []
    for res in cosinusResults:
        if res['cosinus'] > threshold:
            result.append(res)
    return result


def relative_threshold(multiplier, cosinusResults):
    threshold = cosinusResults[0]['cosinus'] * multiplier
    return absolute_threshold(threshold, cosinusResults)


# get sorted Cosinus results
# print results depending on Threshold
