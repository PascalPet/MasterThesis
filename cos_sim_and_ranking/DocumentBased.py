import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity


def get_cosinus(cos):
    return cos['cosinus']


def get_cossim_document_based(filename):
    with open('../pre_processed/LabelEncoding/Label_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
        labelEmbeddings = pickle.load(pkl)

    with open('../pre_processed/DocumentEncoding/' + filename + '.pickle', 'rb') as pkl:
        documentEmbeddings = pickle.load(pkl)

    unchangedLabelsFile = open('../pre_processed/LabelEncoding/Labels.json')
    unchangedLabels = json.load(unchangedLabelsFile)

    projectDescFile = open('../pre_processed/MergeProjectDescription/100_projects_mergedProjectDescription.json')
    projectDescriptions = json.load(projectDescFile)

    for i_doc in range(len(projectDescriptions)):  # change to len(projectDescriptions)
        all_cos = []
        for i_labels in range(len(unchangedLabels)):
            cos = max(max(cosine_similarity([documentEmbeddings[i_doc]], labelEmbeddings[
                i_labels])))  # labelEmbeddings[i_labels] is an array of splitted labels
            all_cos.append({
                'Label': unchangedLabels[i_labels],
                'cosinus': cos,
            })
        all_cos.sort(key=get_cosinus, reverse=True)

        projectDescriptions[i_doc]['ranking'] = all_cos
    print('Cos Sim finished...')
    return projectDescriptions


#results = get_cossim_document_based()
