import sqlite3

class DB:

    def __init__(self, location: str, maxLimit: int = 0) -> None:
        self.words: list = []

        conn = sqlite3.connect(location)

        cursor = conn.execute(f"select * from companies")
        
        if not maxLimit:
            for company in cursor.fetchall():
                self.words.append( company[1] )
            
        else:
            for table in cursor.fetchmany(maxLimit):
                self.words.append( table )


    def getTable(self) -> list:
        return self.words

    def __repr__(self) -> str:
        return f"<DB: {len(self.words)} items>"