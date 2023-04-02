from seekr.db import DB
from seekr.utils import cleanData
from seekr.vectorizer import TfIdfVectorizer


class Seekr:

    def __init__(self, location: str, tableName: str) -> None:
        db = DB(location, tableName, 10)
        
        self.corpus = cleanData( db.getWords() )
        self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> dict:
        
        vectorizer = TfIdfVectorizer()
        vectorizer.fit_transform(corpus)
        vectorizer.create_feature_matrix()
        vectorizer.show_feature_matrix()