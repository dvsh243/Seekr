from seekr.db import DB
from seekr.utils import cleanData
from seekr.vectorizer import TfidfVectorizer


class Seekr:

    def __init__(self, location: str, tableName: str) -> None:
        db = DB(location, tableName, 10)
        
        self.corpus = cleanData( db.getWords() )
        self.tfidf_matrix = self.vectorize(self.corpus)


    def vectorize(self, corpus: list) -> list[list[int, float]]:
        
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)


        for i in range(len(tfidf_matrix)):
            if i > 10: break

            print(corpus[i].split(' '))
            print(tfidf_matrix[i], end='\n\n')
        
        target = '!J'
        count = 0
        for doc in self.corpus:
            for feature in doc.split(' '):
                if feature == target: count += 1; break
        print(f"feature '{target}' can be found in {count} / {len(self.corpus)} documents")

        return tfidf_matrix