import sqlite3
import re


class DB:

    def __init__(self, location: str, tableName: str, maxLimit: int = 0) -> None:
        self.words = []

        conn = sqlite3.connect('data/companies.sqlite')

        cursor = conn.execute(f"select * from {tableName}")
        
        if not maxLimit:
            for company in cursor.fetchall():
                self.words.append( company[1] )
            
        else:
            for company in cursor.fetchmany(maxLimit):
                self.words.append( company[1] )

    def getWords(self) -> list:
        return self.words

    def __repr__(self) -> str:
        return f"<DB: {len(self.words)} items>"