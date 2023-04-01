from seekr.db import DB
from seekr.utils import cleanData


class Seekr:

    def __init__(self, location: str) -> None:
        db = DB(location, 'companies', 10)
        
        self.words = cleanData( db.getWords() )

        print(self.words)