from textblob import TextBlob
import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('movie_reviews')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

text = "I LOVE @Health4UandPets u guys r the best!!"
blob = TextBlob(text)

print("Sentiment:", blob.sentiment)
print("Noun Phrases:", blob.noun_phrases)
print("Words:", blob.words)