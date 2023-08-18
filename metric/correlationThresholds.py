import math
import pickle
import json

file_bn = open('all_metrics_sorted_by_f1.json')
results = json.load(file_bn)

result_relative = {
    "approach": "relative",
    "thresholds": []
}

result_absolute = {
    "approach": "relative",
    "thresholds": []
}
thresholds = [round(x, 2) for x in [i * 0.05 for i in range(1, 21)]]

for thresh in thresholds:
    result_absolute["thresholds"].append([])
    result_relative["thresholds"].append([])

for file in results:
    if 'relative' in file['approach']:
        result_relative["thresholds"][math.floor(file['threshold']*100/5)-1].append(file['f1'])
    else:
        result_absolute["thresholds"][math.floor(file['threshold']*100/5)-1].append(file['f1'])

        #print(result_relative["thresholds"])
        # result_relative["thresholds"][file['threshold']].append(file['f1'])

for f1 in result_absolute["thresholds"]:
    sum = 0
    for x in f1:
        sum +=x
    print(sum/13)

print('______')

for f1 in result_relative["thresholds"]:
    sum = 0
    for x in f1:
        sum +=x
    print(sum/13)




