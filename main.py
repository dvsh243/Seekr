from seekr import Seekr
import pandas as pd
import time

seekr = Seekr()

df = pd.read_csv('data/cleartrip_hotels.csv')
# print(df.columns)

raw_array = []
for i, x in enumerate(df['property_name']):
    # if i > 5000: break
    if type(x) == str: raw_array.append(x)

seekr.load_from_array(raw_array)


while True:
    print()
    target = input("select term to search : ")
    

    print("\nBTree search :-")
    start_time = time.perf_counter()
    matches = seekr.get_indexes_matches(target, 3)
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')

    
    print("\nexhaustive linear search :-")
    start_time = time.perf_counter()
    matches = seekr.get_matches(target, 3)
    print(f"fetched {len(matches)} results in {str(time.perf_counter() - start_time)[:5]} seconds.", end='\n\n')
    for match in matches: print(str(match[0])[:5], match[1], sep='\t')