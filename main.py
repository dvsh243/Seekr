from seekr import Seekr
import time

seekr = Seekr()

seekr.load_from_db('companies', 'data/companies.sqlite', column = 1)
# seekr.load_from_db('news', 'data/news.sqlite', column = 2)


while True:
    print()
    target = input("select term to search : ")
    

    print("\nBTree search :-")
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = 'btree')
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')

    
    print("\nexhaustive linear search :-")
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = 'linear')
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')