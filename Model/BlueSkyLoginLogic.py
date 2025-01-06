from atproto import Client
from atproto_client.exceptions import UnauthorizedError
from View.LoginWindow import login_window
from tkinter import messagebox

def bluesky_login(username, password):
    client = Client()
    try:
        client.login(username, password)
    except UnauthorizedError as e:
        raise UnauthorizedError(f"Login failed: {e}")
    return client

def perform_login(on_success):
    while True:
        entry_username, entry_password = login_window()
        try:
            client = bluesky_login(entry_username, entry_password)
            print(f"Logged in as: {entry_username}")
            on_success(client)
            break
        except UnauthorizedError as e:
            print(e)
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")