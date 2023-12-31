import pickle
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

pdFile = open('../MergeProjectDescription/100_projects_mergedProjectDescription.json')

docs = json.load(pdFile)

# model = SentenceTransformer('all-mpnet-base-v2')
# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('all-mpnet-base-v2')
documentEmbeddings = []

i = 0
for doc in docs:
    i += 1
    sentence_embeddings = model.encode(doc['about'])
    documentEmbeddings.append(sentence_embeddings)
    print('project ' + str(i) + ' encoded')

with open('100_Document_embedding_all-mpnet-base-v2.pickle', 'wb') as pkl:
    pickle.dump(documentEmbeddings, pkl)

# with open('Document_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
#     doc_embedding = pickle.load(pkl)
