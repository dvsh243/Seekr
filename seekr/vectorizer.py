import collections
import math
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


    def fit_transform(self, corpus: list, analyzer: callable) -> list[list]:
        self.totalDocs = len(corpus)
        self.analyzer: callable = analyzer
        
        self.featureMap = self.get_feature_map(corpus)
        self.featureDocCnt = self.get_feature_doc_count(corpus)

        self.matrix = self.create_matrix(corpus)
        print(f"vectors contains {self.featureIndex} dimentions.")

    
    def create_matrix(self, corpus: list[str]) -> list[list[float]]:

        matrix = []

        for i, document in enumerate(corpus):
            if i % 100 == 0: print(f"completed {str((i / self.totalDocs) * 100)[:5]} %", end='\r')

            matrix.append( self.doc_to_vector(document) )
        
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
                index = self.featureMap[feature]  # put the tfidf value at this column
                IDF = math.log( self.totalDocs / self.featureDocCnt[feature] )
                TF = frequencies[feature] / totalFreq

                vector[index] = TF * IDF
        
        return vector


    # - # - # UTILITY FUNCTIONS # - # - #
    # - # - # - # - # - # - # - # - # - # 

    def get_feature_map(self, corpus: list) -> dict:
        """
        map every feature to a unique ID
        the more the frequency of the feature, the lower its index
        """
        counter = collections.Counter()

        for document in corpus:
            for feature in self.analyzer(document):
                counter[feature] += 1

        to_sort = []
        for key, value in counter.items():
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
