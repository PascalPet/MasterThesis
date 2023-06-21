import nltk
import pickle
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def split_text_into_sentences(text):
    sentences_tokenized = nltk.sent_tokenize(text)
    return sentences_tokenized


def encode_project_descriptions_per_sentence(project_descriptions, model, k):
    encoded_project_descriptions = []
    i = 0
    for project in project_descriptions:
        i += 1
        sentences_encoded = []
        sentences = split_text_into_sentences(project['about'])
        sentences_concatenated = concatenate_sentences(sentences, k)
        for sentence_concatenated in sentences_concatenated:
            sentence_embeddings = model.encode(sentence_concatenated)
            sentences_encoded.append(sentence_embeddings)
        print('project ' + str(i) + ' encoded....')
        encoded_project_descriptions.append(sentences_encoded)
    return encoded_project_descriptions


def concatenate_sentences(strings, k):
    result = []
    n = len(strings)
    for i in range(n - k):
        concatenated = ' '.join(strings[i:i + k + 1])
        result.append(concatenated)
    return result


def run(file_name, k):
    pdFile = open('../MergeProjectDescription/mergedProjectDescription.json')

    docs = json.load(pdFile)

    model = SentenceTransformer('all-mpnet-base-v2')

    encoded_projects = encode_project_descriptions_per_sentence(docs, model, k)

    with open(file_name + '.pickle', 'wb') as pkl:
        pickle.dump(encoded_projects, pkl)


for x in range(6):
    run(str(x + 1) + '_Sentence_Embeddings_all-mpnet-base-v2', x)

# with open('3_Sentence_Embeddings_all-mpnet-base-v2.pickle', 'rb') as pkl:
#    doc_embedding = pickle.load(pkl)
# print(doc_embedding[0][0].shape)
