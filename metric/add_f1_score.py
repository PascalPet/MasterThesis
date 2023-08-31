import json
import numpy as np


def get_file_names():
    files = []
    for app in range(2):
        word = 'sentence' if app == 0 else 'word'
        for thresh in range(2):
            threshold = 'absolute' if thresh == 0 else 'relative'
            for x in range(6):
                files.append('all-mpnet-base-v2_' + str(x + 1) + '_' + word + '_' + threshold)
    files.append('all-mpnet-base-v2_doc_absolute_threshold')
    files.append('all-mpnet-base-v2_doc_relative_threshold')
    return files


def calculate_f1_score(files):
    for file in files:
        filepath = 'metric_values/' + file + '.json'
        file_bn = open(filepath)
        metrics = json.load(file_bn)
        for metric in metrics:
            precision = metric['precision']
            recall = metric['recall']
            if precision + recall == 0:
                metric['f1'] = 0
            else:
                metric['f1'] = 2 * ((precision * recall) / (precision + recall))
        with open(filepath, 'w') as outfile:
            json.dump(metrics, outfile)


def get_all_metric_values():
    all_metrics = []
    file_names = get_file_names()

    for filename in file_names:
        file_path = 'metric_values/' + filename + '.json'
        file_bn = open(file_path)
        metrics = json.load(file_bn)
        for metric in metrics:
            metric['approach'] = filename
            all_metrics.append(metric)
    return all_metrics


def getf1(metric):
    return metric['f1']


def serialize_all():
    metrics = get_all_metric_values()
    metrics.sort(key=getf1, reverse=True)

    with open('all_metrics_sorted_by_f1.json', 'w') as outfile:
        json.dump(metrics, outfile)


def get_all_metrics_sorted_by_f1():
    file_bn = open('all_metrics_sorted_by_f1.json')
    return json.load(file_bn)


def get_approaches(metrics, search_value):
    result = []
    for x in range(len(metrics)):
        metrics[x]['index'] = x
        if search_value in metrics[x]['approach']:
            result.append(metrics[x])
    return result


def get_word_approaches():
    return get_approaches(get_all_metrics_sorted_by_f1(), 'word')


def get_sentence_approaches():
    return get_approaches(get_all_metrics_sorted_by_f1(), 'sentence')


def get_document_approaches():
    return get_approaches(get_all_metrics_sorted_by_f1(), 'doc')


def get_relative_approaches():
    return get_approaches(get_all_metrics_sorted_by_f1(), 'relative')


def get_absolute_approaches():
    return get_approaches(get_all_metrics_sorted_by_f1(), 'absolute')


def h(a):
    return " & " + a


# def get_sentence_approaches
results = get_all_metric_values()

# for i in range(26):
#     print("\\begin{table}[!h]")
#     print("\\caption{10 best word based approaches}")
#     print("\\label{tab:word_approaches_f1}")
#     print("\\centering")
#     print("\\begin{tabular}{l l l l l }")
#     print("\\toprule")
#     print("\\tabhead{Threshold} &\\tabhead{Precision} & \\tabhead{Recall} & \\tabhead{Accuracy} "
#           "& \\tabhead{F1}  \\\\")
#     print("\\midrule")
#     for x in range(i*20, i*20+19):
#         res = results[x]
#         print(str(res['threshold'])
#               + h(str(round(res['precision'], 3)))
#               + h(str(round(res['recall'], 3)))
#               + h(str(round(res['accuracy'], 3)))
#               + h(str(round(res['f1'], 3)))
#               + "\\\\"
#               )
#     print("\\bottomrule \\\\")
#     print("\\end{tabular}")
#     print("\\end{table}")

#print(results)

