from serialization.serialize_deserialize import *





with open('../serialization/finishedData/100projects/all-mpnet-base-v2_100_doc_absolute_threshold0.25.pickle', 'rb') as pkl:
    projects = pickle.load(pkl)

sumP = 0
sumR = 0
counter = 0
for x in projects:
    sumP += len(x["resarch_areas"])
    sumR += len(x["result"])
    counter +=1

print(sumP/counter)
print(sumR/counter)



#print(projects[20:40])