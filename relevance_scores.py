import torch
from transformers import BertTokenizer, BertForSequenceClassification
from pygal.style import NeonStyle
import pygal
# Define the topics and their corresponding labels
topics = ["Health", "Education", "Entertainment", "business","lifestyle"]
label_map = {label: index for index, label in enumerate(topics)}

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(topics))

# Function to get relevance scores for each topic
def get_relevance_scores(text):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Perform inference to get relevance scores
    outputs = model(**inputs)
    logits = outputs.logits

    # Calculate softmax to get probabilities
    probabilities = torch.softmax(logits, dim=1)

    # Convert probabilities to relevance scores
    relevance_scores = [prob.item() for topic,prob in zip(topics, probabilities[0])]
    
    return relevance_scores

print(get_relevance_scores("hi this is talhah"))