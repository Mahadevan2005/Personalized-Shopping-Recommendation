import pandas as pd
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
from collections import defaultdict

data = pd.read_csv("products.csv")


user_clicks = [5, 8] 


def cold_start_recommend(data, top_n=5):
    return data.sort_values(by="popularity_score", ascending=False).head(top_n)


def build_user_profile(clicked_ids, data):
    tags = []
    categories = []
    for pid in clicked_ids:
        product = data[data.product_id == pid]
        if not product.empty:
            tags += product.iloc[0]['tags'].split(',')
            categories.append(product.iloc[0]['category'])
    tag_freq = pd.Series(tags).value_counts()
    return {
        "preferred_tags": list(set(tags)),
        "liked_categories": list(set(categories)),
        "tag_freq": tag_freq
    }

def personalized_recommend(data, profile, top_n=5):
    def score(row):
        tag_match = len(set(row['tags'].split(',')) & set(profile['preferred_tags']))
        cat_match = 1 if row['category'] in profile['liked_categories'] else 0
        return tag_match + cat_match + row['popularity_score'] * 0.01

    data['score'] = data.apply(score, axis=1)
    return data.sort_values(by="score", ascending=False).head(top_n)


def visualize_profile(profile):
    plt.figure(figsize=(8, 4))
    profile['tag_freq'].plot(kind='bar', color='skyblue')
    plt.title("User Preferred Tags")
    plt.ylabel("Frequency")
    plt.xlabel("Tags")
    plt.tight_layout()
    plt.show()


print("\n=== ROUND 1: Cold Start Recommendations ===")
round1 = cold_start_recommend(data)
print(tabulate(round1[['product_id', 'title', 'popularity_score']], headers='keys', tablefmt='fancy_grid'))

print("\n=== Simulated User Clicked on Products ===")
clicked_data = data[data['product_id'].isin(user_clicks)][['product_id', 'title', 'tags', 'category']]
print(tabulate(clicked_data, headers='keys', tablefmt='fancy_grid'))


user_profile = build_user_profile(user_clicks, data)
print("\n=== UPDATED USER PROFILE ===")
print("Preferred Tags:", user_profile['preferred_tags'])
print("Liked Categories:", user_profile['liked_categories'])


visualize_profile(user_profile)


print("\n=== ROUND 2: Personalized Recommendations ===")
round2 = personalized_recommend(data, user_profile)
print(tabulate(round2[['product_id', 'title', 'tags', 'category', 'score']], headers='keys', tablefmt='fancy_grid'))