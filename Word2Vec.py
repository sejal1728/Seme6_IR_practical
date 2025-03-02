import gensim
import gensim.downloader as api
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Load a pre-trained Word2Vec model from Gensim
model = api.load("glove-wiki-gigaword-50")  # Use 'word2vec-google-news-300' for a larger model

# Define a sample text
text = "Machine learning is a popular method for artificial intelligence applications."

# Tokenize and remove stopwords
stop_words = set(stopwords.words("english"))
words = [word.lower() for word in word_tokenize(text) if word.isalnum() and word.lower() not in stop_words]

# Find similar words to a given word
word_to_check = "learning"
if word_to_check in model.key_to_index:
    similar_words = model.most_similar(word_to_check, topn=5)
    print(f"Words similar to '{word_to_check}':", similar_words)
else:
    print(f"'{word_to_check}' not found in the model vocabulary.")

# Compute similarity between two words
word1 = "learning"
word2 = "education"

if word1 in model.key_to_index and word2 in model.key_to_index:
    similarity = model.similarity(word1, word2)  # <-- Corrected here
    print(f"Similarity between '{word1}' and '{word2}': {similarity:.4f}")
else:
    print(f"One or both words '{word1}', '{word2}' are not in the model vocabulary.")
