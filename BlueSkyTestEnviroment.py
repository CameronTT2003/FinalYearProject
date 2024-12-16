from atproto import Client
from BlueSkyUrlBuilder import *
import pandas as pd
import json
import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('movie_reviews')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from textblob import TextBlob


#this will gather my personal login details
df = pd.read_csv('C:/Users/camsp/Documents/QMUL/CS2024/Project/Keys/blueSkyLogin.csv', usecols=['email', 'password'])

#this logs me in
client = Client()
client.login(df.iloc[0,0], df.iloc[0,1])

#this will make a post to my account 
#post = client.send_post('Hello world! I love Juliette')
#print(post.uri)
#print(post.cid)
#url = 'https://bsky.app/profile/illybocean.boontavista.com/post/3laqu7hzvxs24'
url = 'https://bsky.app/profile/camerontt2003.bsky.social/post/3ldh42tm3ls2c'
uri = get_uri(url)
#uri = 'at://illybocean.boontavista.com/app.bsky.feed.post/3laqu7hzvxs24'
#depth = 6
#parent_height = 80

res = client.get_post_thread(uri=uri)
thread = res.thread
print(thread)


def extract_text_from_thread(thread):
    texts = []
    if hasattr(thread, 'record') and hasattr(thread.record, 'text'):
        texts.append(thread.record.text)
    if hasattr(thread, 'replies'):
        for reply in thread.replies:
            texts.extend(extract_text_from_thread(reply.post))
    return texts

# Assuming `thread` is the thread object you provided
initial_text = thread.post.record.text if hasattr(thread, 'post') and hasattr(thread.post, 'record') and hasattr(thread.post.record, 'text') else ""
texts = extract_text_from_thread(thread)
total_polarity = 0
total_subjectivity = 0

# Apply TextBlob to each text and calculate the sentiment scores
for text in texts:
    blob = TextBlob(text)
    total_polarity += blob.sentiment.polarity
    total_subjectivity += blob.sentiment.subjectivity
    print(f"Text: {text}")
    print(f"Sentiment: {blob.sentiment}")

# Calculate the average sentiment scores
average_polarity = total_polarity / len(texts) if texts else 0
average_subjectivity = total_subjectivity / len(texts) if texts else 0
print(f"Initial Text: {initial_text}")
print(f"Average Polarity: {average_polarity}")
print(f"Average Subjectivity: {average_subjectivity}")