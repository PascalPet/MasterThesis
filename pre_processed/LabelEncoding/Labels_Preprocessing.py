import json
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#model = SentenceTransformer('all-mpnet-base-v2')
#model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('all-distilroberta-v1')
#file = open('Labels.json')
#data = json.load(file)


def replace_all_blank(text, dic):
    if 'Science & Technology Other Topics' in text:
        text = text.replace('Other Topics', '')
        return text.strip()
    for i in dic:
        text = text.replace(i, '')
    return text.strip()


def split_string_at_ampersand(label):
    delete_words = ['Sciences', 'Other Topics', 'Science', 'Technology']
    result = replace_all_blank(label, delete_words)

    result = result.replace(',', '&')
    substrings = result.split('&')
    stripped = [s.strip() for s in substrings]
    if stripped[-1] == '':
        return stripped[:-1]
    return stripped


#labels = []
#for i in data:
#    labels.append([i["name"]])

#finalLabels = []
#for label in labels:
#    finalLabels.append(split_string_at_ampersand(label[0]))

#with open('ClearedLabels.json', 'w') as outfile:
#    json.dump(finalLabels, outfile)
#
file = open('ClearedLabels.json')
finalLabels = json.load(file)
#
labelEmbeddings = []
for i in range(len(finalLabels)):
    sentence_embeddings = model.encode(finalLabels[i])
    labelEmbeddings.append(sentence_embeddings)


with open('Label_embedding_all-all-distilroberta-v1.pickle', 'wb') as pkl:
    pickle.dump(labelEmbeddings, pkl)

#with open('Label_embedding_all-all-MiniLM-L6-v2.pickle', 'rb') as pkl:
 #   labelEmbeddings2 = pickle.load(pkl)



