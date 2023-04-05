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
