import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# Load English stop words
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove punctuation and stop words
    tokens = [token for token in tokens if token not in string.punctuation and token not in stop_words]

    return " ".join(tokens)

def extract_topic(text, num_topics=3):
    # Preprocess the text
    preprocessed_text = preprocess_text(text)

    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=50, min_df=0.1, stop_words='english')

    # Fit and transform the text data
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_text])

    # Apply NMF for topic modeling
    nmf = NMF(n_components=num_topics, random_state=1)
    nmf.fit(tfidf_matrix)

    # Get the most relevant topic(s)
    topics = nmf.components_

    # Extract the top words from each topic
    feature_names = tfidf_vectorizer.get_feature_names_out()
    top_words = [feature_names[i] for i in topics.argmax(axis=1)]

    # Combine topic keywords into a single string
    topic_string = ", ".join(top_words)

    return topic_string
