from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "Machine learning is amazing.",
    "Deep learning is a subset of machine learning.",
    "K-means is a clustering algorithm.",
    "Natural language processing is part of AI."
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X)

for i, doc in enumerate(documents):
    print(f"Document {i+1}: Cluster {kmeans.labels_[i]}")
