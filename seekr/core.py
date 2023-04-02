from seekr.db import DB
from seekr.utils import cleanData, ngrams
# from seekr.vectorizer import TfIdfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


class Seekr:

    def __init__(self, location: str, tableName: str) -> None:
        db = DB(location, tableName, 10)
        
        self.corpus = cleanData( db.getWords() )
        self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> dict:
        
        vectorizer = TfidfVectorizer(analyzer = 'word')
        tfidf_matrix = vectorizer.fit_transform(corpus)

        print(f"{len(vectorizer.get_feature_names_out())} unique features.")
        

        for i in range(len(corpus)):
            if i > 10: break

            print(corpus[i])
            print(tfidf_matrix[i], end='\n\n')