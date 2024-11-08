from atproto import Client
import pandas as pd


#this will gather my personal login details
df = pd.read_csv('C:/Users/camsp/Documents/QMUL/CS2024/Project/Keys/blueSkyLogin.csv', usecols=['email', 'password'])

#this logs me in
client = Client()
client.login(df.iloc[0,0], df.iloc[0,1])

#this will make a post to my account 
#post = client.send_post('Hello world!')
#print(post.uri)
#print(post.cid)

