import pickle

with open('serialization/finishedData/all-distilroberta-v1_doc_relative_threshold0.1.pickle', 'rb') as pkl:
    labelEmbeddings = pickle.load(pkl)

union_groundtruth = []
for label_embedding in labelEmbeddings:
    union_groundtruth = list(set(union_groundtruth + label_embedding['resarch_areas']))
print(union_groundtruth)