import nltk
import pickle
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def split_text_into_sentences(text):
    # nltk.download('punkt')
    sentences_tokenized = nltk.sent_tokenize(text)

    return sentences_tokenized


def encode_project_descriptions_per_sentence(project_descriptions):
    encoded_project_descriptions = []
    i = 0
    for project in project_descriptions:
        i+=1
        sentences_encoded = []
        sentences = split_text_into_sentences(project['about'])
        for sentence in sentences:
            sentence_embeddings = model.encode(sentence)
            sentences_encoded.append(sentence_embeddings)
        print('project ' + str(i) + ' encoded....')
        encoded_project_descriptions.append(sentences_encoded)
    return encoded_project_descriptions


# pdFile = open('../MergeProjectDescription/mergedProjectDescription.json')
#
# docs = json.load(pdFile)
#
# model = SentenceTransformer('all-mpnet-base-v2')
#
#
# encoded_projects = encode_project_descriptions_per_sentence(docs)
#
# with open('1_Sentence_Emebdings_all-mpnet-base-v2.pickle', 'wb') as pkl:
#     pickle.dump(encoded_projects, pkl)

with open('1_Sentence_Emebdings_all-mpnet-base-v2.pickle', 'rb') as pkl:
    doc_embedding = pickle.load(pkl)

print(doc_embedding[0][0].shape)
#
# print(doc_embedding)
