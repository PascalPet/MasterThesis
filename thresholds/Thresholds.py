def absolute_threshold(threshold, cosine_results):
    result = []
    for res in cosine_results:
        if res['cosinus'] > threshold:
            result.append(res)
    return result


def relative_threshold(multiplier, cosine_results):
    threshold = cosine_results[0]['cosinus'] * multiplier
    return absolute_threshold(threshold, cosine_results)


# get sorted Cosinus results
# print results depending on Threshold
