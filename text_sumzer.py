
from summarizer import Summarizer

def summarize_text(input_text, reduction_ratio=0):
    # Create a BERT-based summarizer
    model = Summarizer()
    # Summarize the text
    summarized_text = model(input_text, ratio=reduction_ratio)
    return summarized_text



