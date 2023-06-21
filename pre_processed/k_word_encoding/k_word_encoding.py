from nltk.tokenize import word_tokenize
import nltk
import pickle
import json
from sentence_transformers import SentenceTransformer


def split_text_into_words(text):
    words = word_tokenize(text)
    words = [w for w in words if w.isalpha()]
    return words


def concatenate_words(strings, k):
    result = []
    n = len(strings)
    for i in range(n - k):
        concatenated = ' '.join(strings[i:i + k + 1])
        result.append(concatenated)
    return result


def encode_project_descriptions_per_words(project_descriptions, model, k):
    encoded_project_descriptions = []
    i = 0
    for project in project_descriptions:
        i += 1
        words_encoded = []
        words = split_text_into_words(project['about'])
        words_concatenated = concatenate_words(words, k)
        for word_concatenated in words_concatenated:
            word_embeddings = model.encode(word_concatenated)
            words_encoded.append(word_embeddings)
        print('project ' + str(i) + ' encoded....')
        encoded_project_descriptions.append(words_encoded)
        if i == 2:
            break
    return encoded_project_descriptions


def run(file_name, k):
    pdFile = open('../MergeProjectDescription/mergedProjectDescription.json')

    docs = json.load(pdFile)

    model = SentenceTransformer('all-mpnet-base-v2')

    encoded_projects = encode_project_descriptions_per_words(docs, model, k)

    with open(file_name + '.pickle', 'wb') as pkl:
        pickle.dump(encoded_projects, pkl)


for x in range(6):
    run(str(x + 1) + '_Word_Embeddings_all-mpnet-base-v2', x)


