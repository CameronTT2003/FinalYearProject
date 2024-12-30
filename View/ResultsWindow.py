import tkinter as tk
from textblob import TextBlob

def create_label(root, text, row, column, columnspan=1):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=column, columnspan=columnspan, sticky="w", padx=10, pady=5)
    return label

def set_initial_text(label, initial_text):
    label.config(text=initial_text)

def set_texts(average_polarity_display, average_subjectivity_display, texts):
    total_polarity = 0
    total_subjectivity = 0

    for text in texts:
        blob = TextBlob(text)
        total_polarity += blob.sentiment.polarity
        total_subjectivity += blob.sentiment.subjectivity

    average_polarity = total_polarity / len(texts) if texts else 0
    average_subjectivity = total_subjectivity / len(texts) if texts else 0

    average_polarity_display.config(text=str(average_polarity))
    average_subjectivity_display.config(text=str(average_subjectivity))

def results_window(initial_text, texts):
    root = tk.Tk()
    root.title("Results Window")

    initial_text_label = create_label(root, initial_text, 0, 0, columnspan=2)

    average_polarity_label = create_label(root, "Average Polarity:", 1, 0)
    average_polarity_display = create_label(root, "", 1, 1)

    average_subjectivity_label = create_label(root, "Average Subjectivity:", 2, 0)
    average_subjectivity_display = create_label(root, "", 2, 1)

    # Set texts
    set_texts(average_polarity_display, average_subjectivity_display, texts)

    root.mainloop()

if __name__ == "__main__":
    initial_text = "Initial Polarity and Subjectivity"
    texts = ["I love this!", "This is bad."]
    results_window(initial_text, texts)