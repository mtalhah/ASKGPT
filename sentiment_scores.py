from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def get_sentiment_scores(paragraph):
    # Initialize the VADER SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Tokenize the paragraph into sentences
    #sentences = [sent.text for sent in nlp(paragraph).sents]
    sentences=paragraph.split('.')
    # Calculate sentiment scores for each sentence
    sentence_sentiments = []

    for sentence in sentences:
        sentiment_scores = analyzer.polarity_scores(sentence)
        sentence_sentiments.append({
            "sentence": sentence,
            "sentiment_score": sentiment_scores['compound']  # Compound score for overall sentiment
        })
            
    sentiments = [i['sentiment_score'] for i in sentence_sentiments]
    p = 0  # positive
    ne = 0  # negative
    nu = 0  # neutral
    for score in sentiments:
        if score > 0:
            p += 1
        elif score < 0:
            ne += 1
        else:
            nu += 1
    
    return [ne,nu,p]

