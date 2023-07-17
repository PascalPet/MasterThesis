import pickle





with open('serialization/finishedData/doc_absolute/all-mpnet-base-v2_doc_absolute_threshold0.25.pickle', 'rb') as pkl:
    approach = pickle.load(pkl)

print(approach)