import collections
import math

class TfIdfVectorizer:

    def __init__(self) -> None:
        self.corpus = ''


    def fit_transform(self, corpus: list) -> None:
        self.corpus = corpus
        
        IDF_map = self.get_IDF_map()
        self.calculate_TfIdf(IDF_map)
        
        # for _ in corpus:
            # for feature in _.split(' '):
                # self.features.add(feature)

    
    # def get_feature_names(self) -> list:
        # return [feature for feature in self.features]


    # def __repr__(self) -> str:
        # return f"<TfIdfVectorizer: {len(self.IDF_map)} features>"
    

    def get_TF(self, target: str, document: str) -> float:
        """
        TF: Term Frequency, which measures how frequently a term occurs 
        in a document. Since every document is different in length, it is 
        possible that a term would appear much more times in long documents 
        than shorter ones. Thus, the term frequency is often divided by the document 
        length (aka. the total number of terms in the document) as a way of normalization:
        TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
        """
        
        target_freq = 0
        terms = document.split(' ')

        for term in terms:
            if term == target: target_freq += 1
        
        return target_freq / len(terms)


    def get_IDF_map(self) -> dict:
        """
        IDF: Inverse Document Frequency, which measures how important a term is. 
        While computing TF, all terms are considered equally important. 
        However it is known that certain terms, such as "is", "of", and "that", 
        may appear a lot of times but have little importance. Thus we need to 
        weigh down the frequent terms while scale up the rare ones, by computing the following:
        IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
        """
        IDF_map = collections.defaultdict(int) # {term: str -> docs: list}

        for document in self.corpus:
            for term in document.split(' '):
                IDF_map[term] += 1

        return IDF_map

    def calculate_TfIdf(self, IDF_map: dict):
        self.featureMap = collections.defaultdict(list) # {doc -> list[ (term, tfidf) ]}

        for docIdx, document in enumerate(self.corpus):
            for term in document.split(' '):
                
                tf = self.get_TF(term, document)
                idf = len(self.corpus) / IDF_map[term]
                # idf = math.log(idf, 2.71828)

                self.featureMap[docIdx].append( (term, tf * idf) )
        
        print(self.featureMap)