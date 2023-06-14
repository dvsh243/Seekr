from seekr import Seekr
import time

seekr = Seekr()
index_type = input("-> enter an index type (linear/kmeans/annoy) : ")
maxLimit = int( input("-> enter number of documents : ") )

seekr.load_from_db('companies', 'data/companies.sqlite', column = 1, maxLimit = maxLimit)
seekr.create_index(index_type)  # 'kmeans' or 'annoy'


while True:
    print()
    target = input("-> select term to search : ")
    

    print("\nBTree search :-" if index_type == 'annoy' else "\nClustered search :-")
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = index_type)
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')

    
    print("\nexhaustive linear search :-")
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = 'linear')
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')