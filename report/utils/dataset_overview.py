import sqlite3

rows: list = []

conn = sqlite3.connect("data/companies.sqlite")
cursor = conn.execute(f"select * from companies")
        
for table in cursor.fetchmany(15):
    print(table)