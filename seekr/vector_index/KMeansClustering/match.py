# from seekr.vector_index.KMeansClustering.k_means_clustering import KMeansClustering

# class KMeansMatch(KMeansClustering):

#     def __init__(self, vectors: list[list], k: int = 10) -> None:
#         super().__init__(vectors, k)

#         print("vector index created.")
        
#         for i, cluster in enumerate(self.clusterList):
#             print(f"cluster {i} containing {len(self.clusterList[cluster])} members")



from sklearn.cluster import KMeans
import collections

class KMeansMatch:

    def __init__(self, vectors: list[list], k: int = 20) -> None:
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(vectors)

        print(kmeans.cluster_centers_.shape)
        print( collections.Counter(kmeans.labels_) ) 
