import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from textblob import TextBlob

# Model imports
from Model.BlueSkyUrlBuilder import get_bluesky_uri
from Model.BlueSkyLoginLogic import perform_login
from Model.BlueSkyTextBuilder import extract_replies_from_thread

# View imports
from View.UrlWindow import url_input_window
from View.LoginWindow import login_window
from View.ResultsWindow import results_window


class BlueSkyController:

    def __init__(self):
        self.client = None
        self.uri = None
        self.initial_text = None
        self.texts = None
        self.login()
        self.get_uri()
        self.get_thread()
        self.show_results()

    def login(self):
        self.client = perform_login()

    def get_uri(self):
        url = url_input_window()
        uri = get_bluesky_uri(url)
        self.uri = uri

    def get_thread(self):
        res = self.client.get_post_thread(uri=self.uri)
        thread = res.thread
        initial_text, texts = extract_replies_from_thread(thread)
        self.initial_text = initial_text
        self.texts = texts
        print(self.initial_text)
        print(self.texts)  

    def show_results(self):
        results_window(self.initial_text, self.texts)

if __name__ == "__main__":
    controller = BlueSkyController()