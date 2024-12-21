import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import os

def create_main_window():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x300")
    return root

def browse_file(label_file_selected, entry_username, entry_password):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        label_file_selected.config(text=f"File Selected: {file_name}")
        df = pd.read_csv(file_path, usecols=['email', 'password'])
        entry_username.delete(0, tk.END)
        entry_username.insert(0, df['email'][0])
        entry_password.delete(0, tk.END)
        entry_password.insert(0, df['password'][0])

def create_login_setup(root, on_login):
    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Create login button
    login_button = tk.Button(root, text="Login", command=lambda: on_login(entry_username, entry_password))
    login_button.pack(pady=20)

    # Create browse button and label for file selected
    label_file_selected = tk.Label(root, text="No file selected")
    label_file_selected.pack(pady=5)
    browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(label_file_selected, entry_username, entry_password))
    browse_button.pack(pady=5)

    return entry_username, entry_password

def handle_login(entry_username, entry_password, root, result):

    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty")
        return
    
    result['username'] = entry_username.get()
    result['password'] = entry_password.get()
    # login logic
    #messagebox.showinfo("Login Info", f"Username: {result['username']}\nPassword: {result['password']}")
    root.destroy()  # Close the window after login

def login_window():
    root = create_main_window()
    result = {}
    entry_username, entry_password = create_login_setup(root, lambda entry_username, entry_password: handle_login(entry_username, entry_password, root, result))
    root.mainloop()
    return result['username'], result['password']
