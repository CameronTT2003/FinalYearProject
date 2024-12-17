import tkinter as tk
from tkinter import messagebox

def main_window(root):
    # Create the main window
    root.title("Login")
    root.geometry("300x200")  # Set the window size to 300x200 pixels
    return root

def login_setup(root, on_login):
    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Create login button
    login_button = tk.Button(root, text="Login", command=lambda: on_login(entry_username, entry_password))
    login_button.pack(pady=20)

def bluesky_login(entry_username, entry_password, root, result):
    result['username'] = entry_username.get()
    result['password'] = entry_password.get()
    # Here you can add your login logic
    messagebox.showinfo("Login Info", f"Username: {result['username']}\nPassword: {result['password']}")
    root.destroy()  # Close the window after login

def bluesky_login_window():
    root = tk.Tk()
    root = main_window(root)
    result = {}
    login_setup(root, lambda entry_username, entry_password: bluesky_login(entry_username, entry_password, root, result))
    root.mainloop()
    return result['username'], result['password']