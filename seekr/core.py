from seekr.db import DB
from seekr.utils import cleanData, word
from seekr.vectorizer import TfidfVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer


class Seekr:

    def __init__(self, location: str, tableName: str) -> None:
        db = DB(location, tableName, 10000)
        
        self.corpus = cleanData( db.getWords() )
        self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> dict:
        
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)

        for i in range(len(tfidf_matrix)):
            if i > 10: break
            
            print(corpus[i].split(' '))
            print(tfidf_matrix[i], end='\n\n')