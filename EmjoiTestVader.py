#python -m pip install emoji vaderSentiment
import emoji
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def demojize_text(text):
    return emoji.demojize(text)

def analyze_sentiment_emoji(text):
    # Demojize the text
    demojized_text = demojize_text(text)
    print(demojized_text)
    
    # Analyze the demojized text sentiment using VADER
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(demojized_text)

    return sentiment

def analyze_sentiment(text):
    

    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)

    return sentiment

if __name__ == "__main__":
    text = "I love this 😊"
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")