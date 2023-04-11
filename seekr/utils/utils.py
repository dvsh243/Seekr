import re

def cleanDocument(document: str) -> str:
    document = document.lower()
    return re.sub(r'[,\'./()]|\sBD',r'', document)

