from seekr.db import DB



class Seekr:

    def __init__(self, location: str) -> None:
        
        db = DB('data/companies.sqlite', 'companies', 100)
        print(db)
