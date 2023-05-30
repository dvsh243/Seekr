from seekr import Seekr
import time


def search(maxLimit):
    seekr = Seekr()

    seekr.load_from_db('companies',
                       'data/companies.sqlite',
                       column=1,
                       maxLimit=maxLimit)

    start_time = time.perf_counter()
    seekr.create_index('annoy')
    index_creation_time = str(time.perf_counter() - start_time)[:5]

    return index_creation_time


test = [100, 500 ,1000, 5000, 10000, 15000, 20000, 30000, 50000]
results = []

for maxLimit in test:
    print(f"\nselecting maxLimit --> {maxLimit}")
    results.append((maxLimit, search(maxLimit)))

print(results)

# annoy index creation time
# 100 -> 0.384
# 1,000 -> 0.733
# 5,000 -> 33.05
# 10,000 -> 103
# 15,000 -> 176
# 20,000 -> 267
# 30,000 -> 441
# 50,000 -> 612