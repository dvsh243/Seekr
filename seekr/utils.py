import re

def cleanData(words: str) -> str:
    return re.sub(r'[,\'./()]|\sBD',r'', words)