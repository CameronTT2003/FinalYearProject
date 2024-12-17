from atproto import Client
from BlueSkyUrlBuilder import *
from BlueSkyLogin import *
import pandas as pd
from textblob import TextBlob

entry_username, entry_password = bluesky_login_window()
print(entry_username)
