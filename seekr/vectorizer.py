import collections
import math

class TfidfVectorizer:
    
    # take 'INC' for example,
    # out of 100,000 documents, 'INC' shows up in 19375 of them
    # therefore, IDF = 100,000 / 19375 = 5.161290
    # IDF = log[base e](5.161290) = 1.64118

    # now consider document 1, '!J INC',
    # out of the 2 words in document 1, 'INC' is one of them,
    # therefore, TF = 1 / 2 = 0.5

    def __init__(self) -> None:
        self.tfidf_matrix = []
        self.totalDocs = 0

    def fit_transform(self, corpus: list) -> list[list]:
        # need to add func analyzer dynamically instead of .split(' ')
        
        self.corpus = corpus
        self.totalDocs = len(corpus)

        self.featureIdxMap = self.create_featureMap()
        self.featureDocCnt = self.create_feature_doc_count()

        min_val, max_val = self.create_tfidf_matrix()
        # self.normalize_matrix(min_val, max_val)

        return self.tfidf_matrix
    

    def create_featureMap(self) -> dict:
        """
        Assigning a unique integer value to each feature to be assigned a column in tfidf_matrix.
        """
        featureIdxMap = {}

        index = 0
        for document in self.corpus:
            for feature in document.split(' '):
                if feature in featureIdxMap: continue
                featureIdxMap[feature] = index
                index += 1

        return featureIdxMap
    

    def create_feature_doc_count(self) -> dict:
        """
        Creating hashMap for feature mapped to number of documents it has been used in.
        """
        featureDocCnt = collections.defaultdict(int)

        for document in self.corpus:
            seen = set()

            for feature in document.split(' '):
                if feature in seen: continue

                featureDocCnt[feature] += 1
                seen.add(feature)  # to avoid duplicate features in the same document
        
        return featureDocCnt
    

    def get_featureCnt_of_doc(self, document) -> tuple[set, int]:
    
        featureCnt = collections.defaultdict(int)
        totalFeatures = 0

        for feature in document.split(' '):
            featureCnt[feature] += 1
            totalFeatures += 1

        return {f: c for f, c in featureCnt.items()}, totalFeatures
    

    def create_tfidf_matrix(self) -> tuple[float, float]:
        min_tfidf, max_tfidf = float('inf'), 0
        
        for document in self.corpus:
            featureCnt, total = self.get_featureCnt_of_doc(document)

            # tfidr_list = [0 for _ in range(len(self.featureIdxMap))]
            tfidf_list = []

            for feature in featureCnt:
                tf = featureCnt[feature] / total
                idf =  self.totalDocs / self.featureDocCnt[feature]
                idf = math.log(idf)  # base e

                # append (featureIndex, tfidf value)
                tfidf_list.append( [self.featureIdxMap[feature], tf * idf] )

                min_tfidf = min(min_tfidf, tf * idf); max_tfidf = max(max_tfidf, tf * idf)
        
            self.tfidf_matrix.append(tfidf_list)

        return min_tfidf, max_tfidf
    

    def normalize_matrix(self, min_val: float = 0, max_val: float = 1) -> None:
        """
        list = [1, 9, 10],      min=1, max=10
        list[0] = (1 - 1) / (10 - 1)
        list[i] = (list[i] - min) / (max - min)
        """

        for i in range(len(self.tfidf_matrix)):
            for j in range(len(self.tfidf_matrix[i])):
            
                self.tfidf_matrix[i][j][1] = (self.tfidf_matrix[i][j][1] - min_val) / (max_val - min_val)
                # print(self.tfidf_matrix[i][j], end='  -  ')
            
            # print()
