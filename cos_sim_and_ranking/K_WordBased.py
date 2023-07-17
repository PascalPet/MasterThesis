import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity


def get_cosinus(cos):
    return cos['cosinus']


def get_cossim_word_based(filename):
    with open('../pre_processed/LabelEncoding/Label_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
        labelEmbeddings = pickle.load(pkl)

    #pre_processed/k_sentence_encoding/2_Sentence_Embeddings_all-mpnet-base-v2.pickle
    with open('../pre_processed/k_word_encoding/' + filename + '.pickle', 'rb') as pkl:
        word_embeddings = pickle.load(pkl)

    unchangedLabelsFile = open('../pre_processed/LabelEncoding/Labels.json')
    unchangedLabels = json.load(unchangedLabelsFile)

    projectDescFile = open('../pre_processed/MergeProjectDescription/mergedProjectDescription.json')
    projectDescriptions = json.load(projectDescFile)

    for i_doc in range(len(projectDescriptions)):  # change to len(projectDescriptions)
        all_cos = []
        for i_labels in range(len(unchangedLabels)):
            highest_score = -1
            for words in word_embeddings[i_doc]:
                cos = max(max(cosine_similarity([words], labelEmbeddings[i_labels])))
                if cos > highest_score:
                    highest_score = cos
            all_cos.append({
                'Label': unchangedLabels[i_labels],
                'cosinus': highest_score,
            })
        all_cos.sort(key=get_cosinus, reverse=True)

        projectDescriptions[i_doc]['ranking'] = all_cos
    print('Cos Sim finished...')
    return projectDescriptions






