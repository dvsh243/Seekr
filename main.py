from seekr import Seekr
import time

seekr = Seekr('data/companies.sqlite')

while True:
    print()
    target = input("select term to search : ")
    
    start_time = time.perf_counter()
    matches = seekr.get_matches(target, 3)
    print(f"fetched results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')

    for match in matches:
        print(match[0], match[1], sep='\t')
