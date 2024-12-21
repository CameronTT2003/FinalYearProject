from atproto import Client
from BlueSkyUrlBuilder import *
from BlueSkyLoginLogic import *
from UrlWindow import *
from LoginWindow import *
import pandas as pd
from textblob import TextBlob


class BlueSkyController:

    def __init__(self):
        self.client = None
        self.uri = None
        self.login()
        self.get_uri()

    def login(self):
        self.client = perform_login()

    def get_uri(self):
        #need to create interface for this
        url = url_input_window()
        uri = get_bluesky_uri(url)
        self.uri = uri
       

if __name__ == "__main__":
    controller = BlueSkyController()