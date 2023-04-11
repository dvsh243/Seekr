import collections
import math
from seekr.utils import to_sparse
# import numpy as np


class TfidfVectorizer:
    
    # take 'INC' for example,
    # out of 100,000 documents, 'INC' shows up in 19375 of them
    # therefore, IDF = 100,000 / 19375 = 5.161290
    # IDF = log[base e](5.161290) = 1.64118

    # now consider document 1, '!J INC',
    # out of the 2 words in document 1, 'INC' is one of them,
    # therefore, TF = 1 / 2 = 0.5

    def __init__(self) -> None:
        self.featureIndex = 0  # number of unique features / dimentions in vectors
        self.totalDocs = 0  # total number of documents / vectors
        pass


    def fit_transform(self, corpus: list, analyzer: callable, skip_k: int = 1) -> list[list]:
        self.totalDocs = len(corpus)
        self.analyzer: callable = analyzer
        
        self.featureMap = self.get_feature_map(corpus, k = skip_k)
        self.featureDocCnt = self.get_feature_doc_count(corpus)

        self.matrix = self.create_matrix(corpus)
        print(f"vectors contains {self.featureIndex} dimentions.")

    
    def create_matrix(self, corpus: list[str]) -> list[list[float]]:

        matrix = []

        for i, document in enumerate(corpus):
            if i % 100 == 0: print(f"completed {str((i / self.totalDocs) * 100)[:5]} %", end='\r')

            matrix.append( to_sparse( self.doc_to_vector(document) ) )  # stores a sparse vector

        return matrix
        # return np.matrix(matrix)  # conversion to numpy matrix takes alot of time

    
    def doc_to_vector(self, document: str) -> list[float]:

        frequencies = collections.defaultdict(int)
        for feature in self.analyzer(document):
            frequencies[feature] += 1
        totalFreq = sum(frequencies.values())
        
        vector = [0 for _ in range(self.featureIndex)]

        for feature in self.analyzer(document):
            
            if feature in self.featureMap:
                index = self.featureMap[feature]  # put the tfidf value at this column of the vector
                IDF = math.log( self.totalDocs / self.featureDocCnt[feature] )
                TF = frequencies[feature] / totalFreq

                vector[index] = TF * IDF

            else: pass 
            # [OPTIMIZE] columns which are not present in corpus, are not added as dimentions,
            # resulting in lower euclidian distance but optimized comparison
        
        return vector


    # - # - # UTILITY FUNCTIONS # - # - #
    # - # - # - # - # - # - # - # - # - # 

    def get_feature_map(self, corpus: list, k: int = 0) -> dict:
        """
        k: int, if feature has <= k frequency in the whole corpus, it isnt added as a dimension in the vectors
        map every feature to a unique ID
        the more the frequency of the feature, the lower its index
        """
        counter = collections.Counter()

        for document in corpus:
            for feature in self.analyzer(document):
                counter[feature] += 1

        to_sort = []
        for key, value in counter.items():
            if value <= k: continue  # [OPTIMIZE] reduces dimensions in vector, but with tradeoff that it cannot fuzzy search for unique features that occur only once in the whole corpus
            to_sort.append( (value, key) )  # (count, feature) pair
        to_sort.sort(reverse = True)

        featureMap = {}
        for _, feature in to_sort:
            featureMap[feature] = self.featureIndex
            self.featureIndex += 1
        
        return featureMap


    def get_feature_doc_count(self, corpus: list) -> dict:
        """
        how many has documents has feature `feature` been used in 
        """
        featureDocCnt = collections.defaultdict(int)

        for document in corpus:
            seen = set()

            for feature in self.analyzer(document):
                if feature in seen: continue

                featureDocCnt[feature] += 1
                seen.add(feature)  # to avoid duplicate features in the same document
        
        return featureDocCnt
