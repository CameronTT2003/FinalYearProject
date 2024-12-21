import tkinter as tk
from tkinter import messagebox

def create_main_window():
    root = tk.Tk()
    root.title("URL Input")
    root.geometry("400x200")
    return root

def create_url_input_setup(root, on_submit):
    tk.Label(root, text="Enter URL:").pack(pady=5)
    entry_url = tk.Entry(root, width=50)
    entry_url.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(entry_url))
    submit_button.pack(pady=20)

    return entry_url

def handle_submit(entry_url, root, result):
    url = entry_url.get()
    
    if not url:
        messagebox.showerror("Error", "URL cannot be empty")
        return
    
    result['url'] = url
    root.destroy()  # Close the window after submission

def url_input_window():
    root = create_main_window()
    result = {}
    entry_url = create_url_input_setup(root, lambda entry_url: handle_submit(entry_url, root, result))
    root.mainloop()
    return result.get('url')


if __name__ == "__main__":
    url = url_input_window()
    print(f"URL entered: {url}")