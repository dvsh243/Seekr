# from seekr.vector_index.KMeansClustering.k_means_clustering import KMeansClustering

# class KMeansMatch(KMeansClustering):

#     def __init__(self, vectors: list[list], k: int = 10) -> None:
#         super().__init__(vectors, k)

#         print("vector index created.")
        
#         for i, cluster in enumerate(self.clusterList):
#             print(f"cluster {i} containing {len(self.clusterList[cluster])} members")



# from sklearn.cluster import KMeans
from gensim.models import KeyedVectors  # uses HNSW
import collections

class KMeansMatch:

    def __init__(self, vectors: list[list], k: int = 20) -> None:

        self.kv = KeyedVectors(len(vectors[0]))
        self.kv.add_vectors([i for i in range(len(vectors))], vectors)


    def match(self, target_tfidf_dense: list):

        # self.kv.add_vector(-1 , target_tfidf_dense)
        # return self.kv.most_similar(-1, topn=5)

        # return self.kv.similar_by_vector(target_tfidf_dense, topn = 5)

        return self.kv.most_similar(positive = [target_tfidf_dense], topn = 5)
