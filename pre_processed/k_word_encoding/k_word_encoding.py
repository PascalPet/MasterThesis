from nltk.tokenize import word_tokenize
import nltk
import pickle
import json
from sentence_transformers import SentenceTransformer

texta = "God is Great! I won a lottery."


def split_text_into_words(text):
    words = word_tokenize(text)
    words = [w for w in words if w.isalpha()]
    return words


def encode_project_descriptions_per_words(project_descriptions):
    encoded_project_descriptions = []
    i = 0
    for project in project_descriptions:
        i += 1
        words_encoded = []
        words = split_text_into_words(project['about'])
        for word in words:
            word_embeddings = model.encode(word)
            words_encoded.append(word_embeddings)
        print('project ' + str(i) + ' encoded....')
        encoded_project_descriptions.append(words_encoded)
    return encoded_project_descriptions


pdFile = open('../MergeProjectDescription/mergedProjectDescription.json')

docs = json.load(pdFile)

model = SentenceTransformer('all-mpnet-base-v2')


encoded_projects = encode_project_descriptions_per_words(docs)

with open('1_Word_Emebdings_all-mpnet-base-v2.pickle', 'wb') as pkl:
    pickle.dump(encoded_projects, pkl)
