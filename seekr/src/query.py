from seekr.utils.utils import cleanDocument
from seekr.src.loss_functions import distance
from seekr.src.vectorizer import TfidfVectorizer
import heapq


class Query:

    def __init__(self, corpus: list, vectorizer: TfidfVectorizer, index, totalFeatures: int, limit: int) -> None:
        self.vectorizer = vectorizer
        self.totalFeatures = totalFeatures
        self.limit = limit
        self.corpus = corpus
        self.index = index


    def query(self, target: str, index_type: str):

        if index_type == 'linear':
            res = self.ExhaustiveSearch(target)
        elif index_type == 'annoy':
            res = self.BTreeSearch(target)
        elif index_type == 'kmeans':
            res = self.KMeansSearch(target)
            
        return res


    def ExhaustiveSearch(self, target: str):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)

        similarity = []  # min heap

        for index, doc_vector in enumerate(self.vectorizer.matrix):
            # if index % 100 == 0: print(f"compared {str((index / len(self.corpus)) * 100)[:5]} %", end='\r')

            heapq.heappush(
                similarity,
                ( distance.euclidian_distance(
                        vector1 = target_vector, 
                        vector2 = doc_vector, 
                        dimentions = self.totalFeatures,
                    ), 
                    index 
                )
            )

        res = []
        for _ in range( min(len(similarity), self.limit) ):
            sim_value, index = heapq.heappop(similarity)
            res.append( (sim_value, self.corpus[index]) )
        return res

    
    def BTreeSearch(self, target: str):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)
        leaf_indexes = self.index.find_leaf(target_vector)
        # print(f"found {len(leaf_indexes)} vectors to search.\nleaf_indexes -> {leaf_indexes[:5]}")

        res = []
        for distance, index, vector in self.index.find_closest_vectors(target_vector, leaf_indexes, self.limit):
            res.append( (distance, self.corpus[index]) )
        return res
    

    def KMeansSearch(self, target: str):
        target = cleanDocument(target)
        target_vector = self.vectorizer.doc_to_vector(target)

        res = []
        for distance, index in self.index.find_closest_vectors(target_vector, self.limit):
            res.append( (distance, self.corpus[index]) )
        return res



