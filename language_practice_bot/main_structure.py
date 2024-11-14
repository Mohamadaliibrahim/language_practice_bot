import tkinter as tk
from tkinter import messagebox
import random
import json

# Load the vocabulary
with open('vocabulary.json', 'r', encoding='utf-8') as file:
    vocabulary = json.load(file)

# Initialize the main application window
root = tk.Tk()
root.title("Language Practice Bot")
root.geometry("600x400")

def start_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(root, text="Welcome to the Language Practice Bot!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    instructions_label = tk.Label(root, text="You can practice translating English words into another language.")
    instructions_label.pack(pady=10)

    start_button = tk.Button(root, text="Start", command=choose_language)
    start_button.pack(pady=20)

def choose_language():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    languages = ["Spanish", "French", "German", "Italian"]

    language_label = tk.Label(root, text="Please choose a language to practice:", font=("Helvetica", 14))
    language_label.pack(pady=20)

    for language_option in languages:
        lang_button = tk.Button(root, text=language_option, width=15,
                                command=lambda lang=language_option: start_quiz(lang))
        lang_button.pack(pady=5)

def start_quiz(selected_language):
    global language, filtered_vocabulary, score, total_questions, words_asked

    language = selected_language
    score = 0
    total_questions = 0
    words_asked = []

    # Filter vocabulary
    filtered_vocabulary = {
        word: translations for word, translations in vocabulary.items()
        if language in translations and translations[language]
    }

    if not filtered_vocabulary:
        messagebox.showerror("Error", f"No words available for {language}")
        start_screen()
        return

    ask_question()

def ask_question():
    global current_word, correct_translation, options

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    if len(words_asked) == len(filtered_vocabulary):
        show_result()
        return

    # Choose a random word that hasn't been asked yet
    current_word = random.choice(list(filtered_vocabulary.keys()))
    while current_word in words_asked:
        current_word = random.choice(list(filtered_vocabulary.keys()))
    words_asked.append(current_word)

    correct_translation = filtered_vocabulary[current_word][language]

    # Generate incorrect options
    all_translations = [
        v[language] for v in filtered_vocabulary.values()
        if v[language] != correct_translation
    ]

    num_options = min(3, len(all_translations))
    incorrect_options = random.sample(all_translations, num_options)

    # Combine and shuffle options
    options = incorrect_options + [correct_translation]
    random.shuffle(options)

    # Display the question
    question_label = tk.Label(root, text=f"Translate '{current_word}' into {language}:", font=("Helvetica", 14))
    question_label.pack(pady=20)

    # Variable to store user's choice
    user_choice = tk.StringVar()

    # Display options as radio buttons
    for option in options:
        option_button = tk.Radiobutton(root, text=option, variable=user_choice, value=option, font=("Helvetica", 12))
        option_button.pack(pady=5)

    # Frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    submit_button = tk.Button(button_frame, text="Submit", command=lambda: check_answer(user_choice.get()))
    submit_button.pack(side='left', padx=10)

    stop_button = tk.Button(button_frame, text="Stop Quiz", command=confirm_stop_quiz)
    stop_button.pack(side='left', padx=10)

def confirm_stop_quiz():
    response = messagebox.askyesno("Confirm", "Are you sure you want to stop the quiz?")
    if response:
        show_result()

def check_answer(selected_option):
    global score, total_questions

    total_questions += 1

    if selected_option == correct_translation:
        score += 1
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect", f"Wrong answer.\nThe correct translation is '{correct_translation}'.")

    ask_question()

def show_result():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    result_label = tk.Label(root, text=f"You got {score} out of {total_questions} correct!", font=("Helvetica", 16))
    result_label.pack(pady=30)

    restart_button = tk.Button(root, text="Play Again", command=start_screen)
    restart_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

if __name__ == "__main__":
    start_screen()
    root.mainloop()
