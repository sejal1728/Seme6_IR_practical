import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "this is the first document",
    "and this is the second document",
    "also have the third document",
    "this is the fourth document"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)

# Rows where 'this' AND 'first' are present
AllAND = df[(df['this'] == 1) & (df['first'] == 1)]
print("Indices where 'this' AND 'first' present:", AllAND.index.to_list())

# Rows where 'this' OR 'first' are present
AllOR = df[(df['this'] == 1) | (df['first'] == 1)]
print("Indices where 'this' OR 'first' present:", AllOR.index.to_list())

# Rows where 'and' is NOT present
ALLnot = df[df['and'] == 0]
print("Indices where 'and' is NOT present:", ALLnot.index.to_list())
