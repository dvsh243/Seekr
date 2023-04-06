import sqlite3

class DB:

    def __init__(self, location: str, maxLimit: int = 0) -> None:
        self.rows: list = []

        conn = sqlite3.connect(location)

        cursor = conn.execute(f"select * from companies")
        
        if not maxLimit:
            for table in cursor.fetchall():
                self.rows.append( table )
            
        else:
            for table in cursor.fetchmany(maxLimit):
                self.rows.append( table )


    def getTable(self) -> list[tuple]:
        return self.rows

    def __repr__(self) -> str:
        return f"<DB: {len(self.rows)} items>"
    
    

class CSV:

    def __init__(self, location: str, maxLimit: int = 0) -> None:
        self.rows = []

        i = 0
        for row in open(location, 'r'):
            if i == 0: i += 1; continue # contains only column names
            if maxLimit and i > maxLimit: break
            row = row.split(',')
            row[-1] = row[-1].replace('\n', '')

            self.rows.append(row)
            i += 1

    def getTable(self) -> list[list]:
        return self.rows

    def __repr__(self) -> str:
        return f"<CSV: {len(self.rows)} items>"
