from serialization.serialize_deserialize import *





with open('../serialization/finishedData/100projects/all-mpnet-base-v2_100_doc_absolute_threshold0.25.pickle', 'rb') as pkl:
    projects = pickle.load(pkl)

print(projects[23:40])