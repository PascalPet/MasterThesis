import random
from cos_sim_and_ranking.DocumentBased import *
from serialization.serialize_deserialize import *

import numpy as np


def apk(actual, predicted, k):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted):
        # first condition checks whether it is valid prediction
        # second condition checks if prediction is not repeated
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    return score / min(len(actual), k)


def mapk(actual, predicted, k):
    return np.mean([apk(a, p, k) for a, p in zip(actual, predicted)])


def calculate_avg_mapk(projects_with_ranking):
    project_counter = 0
    value = 0
    for project in projects_with_ranking[:3]:
        project_counter += 1
        ranking = [obj['Label'] for obj in project['ranking']]
        value += mapk(project['resarch_areas'], ranking, len(ranking))
    return value / project_counter


projects = deserialize_results('all-MiniLM-L6-v2_doc_relative_threshold0.1')
print(calculate_avg_mapk(projects))

projects2 = deserialize_results('all-mpnet-base-v2_doc_relative_threshold0.1')
print(calculate_avg_mapk(projects2))

projects3 = deserialize_results('all-distilroberta-v1_doc_relative_threshold0.1')
print(calculate_avg_mapk(projects3))
