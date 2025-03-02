import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def custom_cosine_similarity(x, y):
    if len(x) != len(y):
        return None

    dot_product = np.dot(x, y)
    magnitude_x = np.sqrt(np.sum(x**2))
    magnitude_y = np.sqrt(np.sum(y**2))

    cosine_sim = dot_product / (magnitude_x * magnitude_y)
    return cosine_sim


corpus = [
    "apple orange banana",
    "banana orange grape",
    "grape mango apple",
    "mango apple banana"
]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()


cos_sim_1_2 = custom_cosine_similarity(X[0], X[1])
cos_sim_1_3 = custom_cosine_similarity(X[0], X[3])
cos_sim_2_1 = custom_cosine_similarity(X[2], X[1])

# Display results
print("Cosine Similarity between 1 & 2:", cos_sim_1_2)
print("Cosine Similarity between 1 & 3:", cos_sim_1_3)
print("Cosine Similarity between 2 & 1:", cos_sim_2_1)

