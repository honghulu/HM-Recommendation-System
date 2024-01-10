import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gc

from collections import defaultdict

# synthesize data
NUM_USERS = 10_000
NUM_ITEMS = 1_000
user_id = np.arange(start=0, stop=NUM_USERS)
item_id = np.arange(start=0, stop=NUM_ITEMS)
np.random.seed(42)

user_item_dict = defaultdict(list)
genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Western']
for id in user_id:

    # random the number of item generation
    # for each user, random 3 to 5 items to be rated.
    num_rand_item = np.random.randint(low=3, high=5)

    # random from the item_id
    rand_items = np.random.choice(item_id, size=num_rand_item, replace=False)

    # random rating for each itme_id
    rand_rating = np.random.randint(low=1, high=10, size=num_rand_item)

    # collect the user-item paris.
    for uid, iid, rating in zip([id] * num_rand_item, rand_items, rand_rating):
        user_item_dict['user_id'].append(uid)
        user_item_dict['item_id'].append(iid)
        user_item_dict['rating'].append(rating)

# prepare dataframe
ratings = pd.DataFrame(user_item_dict)
print("Rating Dataframe")
ratings[['user_id', 'item_id']] = ratings[['user_id', 'item_id']].astype(str)
display(ratings.head())

item_genre_dict = defaultdict(list)
for iid in item_id:
    # random number of genres
    num_rand_genre = np.random.randint(low=1, high=3)
    # random set of genres
    rand_genres = np.random.choice(genres, size=num_rand_genre, replace=False)
    item_genre_dict['item_id'].append(iid)
    item_genre_dict['genres'].append(', '.join(list(rand_genres)))

# prepare dataframe
items = pd.DataFrame(item_genre_dict)
print("\nItem Dataframe")
items = items.astype(str)
display(items.head())