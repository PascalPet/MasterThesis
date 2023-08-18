import json
import pickle
#
# c_bn = open('labeled_cleo.json', encoding="utf-8")
# c_labels = json.load(c_bn)
#
# s_bn = open('labeled_simon.json', encoding="utf-8")
# s_labels = json.load(s_bn)

with open('../serialization/finishedData/100projects/all-mpnet-base-v2_100_doc_absolute_threshold0.25.pickle', 'rb') as pkl:
    projects = pickle.load(pkl)


def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    jaccard_coefficient = len(intersection) / len(union)
    return jaccard_coefficient

#print(projects[13])
result = []
sum = 0
for i_project in (range(len(projects))):
    result_labels = [x['Label'] for x in projects[i_project]['result']]
    sim = jaccard_similarity(projects[i_project]['resarch_areas'], result_labels)
    result.append({
        'project_index': i_project,
        'jaccard': sim
    })
    if sim == 1: print(i_project)
    sum += sim

print(result)
print(sum/len(projects))
#print(projects[:50])

# similarity = jaccard_similarity(list1, list2)
# print(similarity)
