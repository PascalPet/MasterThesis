import json

def cardinality(project_descriptions):
    d = len(project_descriptions)
    sum = 0
    for project in project_descriptions:
        sum += len(project['resarch_areas'])
    return sum/d

def density(project_descriptions, labels):
    d = len(project_descriptions)
    l = len(labels)
    sum = 0
    for project in project_descriptions:
        sum += (len(project['resarch_areas']) / len(labels))

    return sum/d

projectDescFile = open('../pre_processed/MergeProjectDescription/mergedProjectDescription.json')
projectDescriptions = json.load(projectDescFile)

unchangedLabelsFile = open('../pre_processed/LabelEncoding/Labels.json')
unchangedLabels = json.load(unchangedLabelsFile)

print('cardinality: ', cardinality(projectDescriptions), 'density: ', density(projectDescriptions, unchangedLabels))

