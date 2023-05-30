# Seekr.

#### In-memory fuzzy matching.

## Usage 
```python
from seekr import Seekr

seekr.load_from_db('companies', 'data/companies.sqlite', column = 1)
seekr.create_index('annoy')   # 'annoy' or 'kmeans'

matches = seekr.query('Active Fund LLC', limit = 3, index_type = 'annoy')  # 'linear', 'annoy', 'kmeans'
```

## How does it work
...


## Tradeoffs

<!-- - Using dense matrix instead of sparse matrix for easy indexing and calculation of dot product and euclidian distance between two vectors.\
dense vector -> `[0, 0, 4.51, 0, 0, 9.23, 0, 0, 0, 0, 0]`\
sparse vector -> `[(2, 4.51), (5, 9.23)]` -->

- Features which occur <= `skip_k` times in the whole corpus aren't added as a dimension in the vector resulting in fast comparison at the tradeoff of querying for unique features that can be found in the document.

- Using `ngrams` to define features instead of `whitespace` which result in more dimension to the vector but more accurate fuzzy searching.\
ngrams of `"EMERGENCY"` -> `['EME', 'MER', 'ERG', 'RGE', 'GEN', 'ENC', 'NCY']`

- During convertion of the target string to vector, `ngrams`/`whitespaces` which are not present in corpus, are not added as dimentions in the resulting vector leading to incorrect euclidian distance but optimized comparison.\
vector of `"!J INC"` will have same euclidian distance to its similar vectors as the vector of `"!J INC )*&!)#!*)^!))!*&*"` 

- `self.matrix` in `TfidfVectorizer` stores sparse vectors instead of dense vectors for memory optimization\
dense vector -> `[0, 0, 4.51, 0, 0, 9.23, 0, 0, 0, 0, 0]`\
sparse vector -> `[(2, 4.51), (5, 9.23)]`

- Indexed vectors using BTree will not give all the similar vectors as given by linear exhaustive searching but indexing is very time efficient.

- Finding centers during indexing multiple times to achieve the most optimum vector clustering.

- `sensitivity` of ANN which describes the ratio of distribution of vectors on either side of the hyperplane. Increasing the sensitivity can slower the index creation.

- instead of actually using the average vector of a cluster for computation, the vector closest the the average vector is chosen because of its less dimensionality


### Appendix

This project was developed as a major project during my college studies.
