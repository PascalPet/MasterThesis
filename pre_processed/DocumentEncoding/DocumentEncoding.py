import pickle
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# pdFile = open('../MergeProjectDescription/mergedProjectDescription.json')
#
# docs = json.load(pdFile)
#
# model = SentenceTransformer('all-mpnet-base-v2')
#
# documentEmbeddings = []
#
# i = 0
# for doc in docs:
#     sentence_embeddings = model.encode(doc['about'])
#     documentEmbeddings.append(sentence_embeddings)
#     if i % 25 == 0:
#         print(i)
#     i += 1
#
#
# with open('Document_embedding_all-mpnet-base-v2.pickle', 'wb') as pkl:
#     pickle.dump(documentEmbeddings, pkl)

with open('Document_embedding_all-mpnet-base-v2.pickle', 'rb') as pkl:
    doc_embedding = pickle.load(pkl)

print(cosine_similarity([doc_embedding[3]], doc_embedding[:4]))
