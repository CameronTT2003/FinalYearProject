from atproto import Client
import pandas as pd
import json


#this will gather my personal login details
df = pd.read_csv('C:/Users/camsp/Documents/QMUL/CS2024/Project/Keys/blueSkyLogin.csv', usecols=['email', 'password'])

#this logs me in
client = Client()
client.login(df.iloc[0,0], df.iloc[0,1])

#this will make a post to my account 
#post = client.send_post('Hello world! I love Juliette')
#print(post.uri)
#print(post.cid)
url = 'https://bsky.app/profile/illybocean.boontavista.com/post/3laqu7hzvxs24'
uri = 'at://illybocean.boontavista.com/app.bsky.feed.post/3laqu7hzvxs24'
#depth = 6
#parent_height = 80

res = client.get_post_thread(uri=uri)
thread = res.thread
#print(thread)




thread_json = json.dumps(thread, default=lambda o: o.__dict__, indent=4)
print(thread_json)


# if 'replies' in thread:
#     for reply in thread['replies']:
#         reply_text = reply.get('post', {}).get('text', 'No text found')
#         print(f"Reply: {reply_text}")
# else:
#     print("No replies found.")