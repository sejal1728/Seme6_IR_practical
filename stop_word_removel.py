import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_text)

# Example usage
text = "This is a simple example to demonstrate stop word removal."
processed_text = remove_stopwords(text)
print(processed_text)
