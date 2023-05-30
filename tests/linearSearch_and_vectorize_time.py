'''from seekr import Seekr
import time

seekr = Seekr()
# index_type = 'kmeans'

seekr.load_from_db('companies', 'data/companies.sqlite', column = 1, maxLimit = 10000)
# seekr.create_index(index_type)  # 'kmeans' or 'annoy'


while True:
    print()
    target = input("select term to search : ")
    

    # print("\nBTree search :-")
    # start_time = time.perf_counter()
    # matches = seekr.query(target, limit = 3, index_type = index_type)  # replace with 'kmeans' or 'annoy'
    # print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    # for match in matches: print(str(match[0])[:5], match[1], sep='\t')

    
    print("\nexhaustive linear search :-")
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = 'linear')
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')'''


from seekr import Seekr
import time

def search(maxLimit):
    seekr = Seekr()

    start_time = time.perf_counter()
    seekr.load_from_db('companies', 'data/companies.sqlite', column = 1, maxLimit = maxLimit)
    vectorize_time = str(time.perf_counter() - start_time)[:5]
    
    target = "Corporation"
    
    start_time = time.perf_counter()
    matches = seekr.query(target, limit = 3, index_type = 'linear')
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')

    search_time = str(time.perf_counter() - start_time)[:5]
    return search_time, vectorize_time
    

test = [100, 500 ,1000, 5000, 10000, 15000, 20000, 30000, 50000]
results = []  # (testVectors, (linearSearchTime, vectorizeTime))
# for k means -> linearSearchTime / number of k means centers
# for annoy -> log base 2 of (linearSearchTime)

# need to calculate index creation time for annoy and kmeans

for maxLimit in test:
    print(f"\nselecting maxLimit --> {maxLimit}")
    results.append( (maxLimit, search(maxLimit)) )

print(results)