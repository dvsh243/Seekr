from seekr import Seekr
import time

seekr = Seekr()
seekr.load_from_db(location = 'data/companies.sqlite', column = 1)


# while True:
#     print()
#     target = input("select term to search : ")
    
#     start_time = time.perf_counter()
#     matches = seekr.get_matches(target, 3)
#     print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')

#     for match in matches:
#         print(str(match[1])[:5], match[0], sep='\t')
