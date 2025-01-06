#python -m pip install emoji textblob
import emoji
from textblob import TextBlob

def demojize_text(text):
    return emoji.demojize(text)

def analyze_sentiment(text):
    # demojize the text
    demojized_text = demojize_text(text)
    print(demojized_text)
    # the demojized text sentiment
    blob = TextBlob(demojized_text)
    sentiment = blob.sentiment

    return sentiment

if __name__ == "__main__":
    text = "i hate this😡"
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")