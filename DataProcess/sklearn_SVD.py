import numpy as np
from sklearn.decomposition import TruncatedSVD

'''
the user_item_matrix will look like this
|        | item 1 | ... | item m |
|--------|--------|-----|--------|
| user 1 | 3      | 0   | 0      |
| ...    | 0      | 4   | 5      |
| user n | 2      | 0   | 0      |
'''

# initial hyperparameter
epsilon = 1e-9
n_latent_factors = 10

# generate item lantent features
item_svd = TruncatedSVD(n_components = n_latent_factors)
item_features = item_svd.fit_transform(user_item_matrix.transpose()) + epsilon

# generate user latent features
user_svd = TruncatedSVD(n_components = n_latent_factors)
user_features = user_svd.fit_transform(user_item_matrix) + epsilon