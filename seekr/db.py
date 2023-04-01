import sqlite3


class DB:

    def __init__(self, location: str, maxLimit: int = 0):
        self.companies = []

        conn = sqlite3.connect('data/companies.sqlite')
        cursor = conn.execute("select * from companies")
        
        if not maxLimit:
            for company in cursor.fetchall():
                self.companies.append( company[1] )
            
        else:
            for company in cursor.fetchmany(maxLimit):
                self.companies.append( company[1] )
        
        print(f"fetched {len(self.companies)} entries.")