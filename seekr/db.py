import sqlite3
import re


class DB:

    def __init__(self, location: str, tableName: str, maxLimit: int = 0) -> None:
        self.items = []

        conn = sqlite3.connect('data/companies.sqlite')
        cursor = conn.execute(f"select * from {tableName}")
        
        if not maxLimit:
            for company in cursor.fetchall():
                self.items.append( company[1] )
            
        else:
            for company in cursor.fetchmany(maxLimit):
                self.items.append( company[1] )
        
        self.cleanData()


    def cleanData(self) -> None:
        for i in range(len(self.items)):
            self.items[i] = re.sub(r'[,-./]|\sBD',r'', self.items[i])

    def getItems(self) -> list:
        return self.items

    def __repr__(self) -> str:
        return f"<DB: {len(self.items)} items>"