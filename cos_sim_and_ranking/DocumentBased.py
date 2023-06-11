import pickle
import json
import sys
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def get_cosinus(cos):
    return cos['cosinus']


def get_cossim():
    with open('pre_processed/LabelEncoding/Label_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
        labelEmbeddings = pickle.load(pkl)

    with open('pre_processed/DocumentEncoding/Document_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
        documentEmbeddings = pickle.load(pkl)

    unchangedLabelsFile = open('pre_processed/LabelEncoding/Labels.json')
    unchangedLabels = json.load(unchangedLabelsFile)

    projectDescFile = open('pre_processed/MergeProjectDescription/mergedProjectDescription.json')
    projectDescriptions = json.load(projectDescFile)

    for i_doc in range(len(projectDescriptions)):
        all_cos = []
        for i_labels in range(len(unchangedLabels)):
            cos = max(max(cosine_similarity([documentEmbeddings[i_doc]], labelEmbeddings[i_labels])))
            all_cos.append({
                'Label': unchangedLabels[i_labels],
                'cosinus': cos,
            })
        all_cos.sort(key=get_cosinus, reverse=True)

        projectDescriptions[i_doc]['ranking'] = all_cos
    print('Cos Sim finished...')
    return projectDescriptions
