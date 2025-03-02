import nltk

# Ensure NLTK uses the correct data path
nltk.data.path.append("C:/Users/sejalpatil1728/AppData/Roaming/nltk_data")

# Now, run your code
from nltk import word_tokenize
from nltk.util import ngrams

text = "this is the simple text for the unigrams , bigrams, ngrams"

tokens = word_tokenize(text.lower())
Unigrams = list(ngrams(tokens, 1))
Bigrams = list(ngrams(tokens, 2))
Ngrams = list(ngrams(tokens, 3))

print("\nOriginal text:", text)
print("\nUnigrams:", Unigrams)
print("\nBigrams:", Bigrams)
print("\nNgrams:", Ngrams)
