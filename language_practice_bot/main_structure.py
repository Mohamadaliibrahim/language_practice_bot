from os import stat_result
import tkinter as tk
from tkinter import messagebox
import random
import json

# Constants
QUESTIONS_PER_LEVEL = 15  # Number of questions per level
LEVELS = ["Beginner", "Intermediate", "Advanced", "Fluent"]
BG_COLOR = '#1E1E2C'       # Dark background color
FG_COLOR = '#EAEAEA'       # Light text color
BTN_COLOR = '#5A9'         # Button background color (calming green)
BTN_TEXT_COLOR = '#FFFFFF' # Button text color (white)
ERROR_COLOR = '#D9534F'    # Error button color (red)
OPTION_COLOR = '#3A3A48'   # Option button background color (slightly darker)
OPTION_SELECTED_COLOR = '#5A9' # Option selected background color

FONT_TITLE = ('Georgia', 18, 'bold')
FONT_TEXT = ('Verdana', 13)
FONT_BTN = ('Verdana', 12, 'bold')
FONT_OPTION = ('Courier', 12, 'italic')

# Load the vocabulary
with open('vocabulary.json', 'r', encoding='utf-8') as file:
    vocabulary = json.load(file)

# Initialize the main application window
root = tk.Tk()
root.title("Language Practice Bot")
root.geometry("600x500")
root.configure(bg=BG_COLOR)

# Variables to track the quiz state
level_index = 0
questions_asked = []
score = 0
total_questions = 0

def start_screen():
    global level_index, questions_asked, score, total_questions

    level_index = 0
    questions_asked = []
    score = 0
    total_questions = 0

    # Clear the window
    for widget in root.winfo_children():

        widget.destroy()

    root.configure(bg=BG_COLOR)

    welcome_label = tk.Label(root, text="Welcome to the Language Practice Bot!", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
    welcome_label.pack(pady=20)
 
    instructions_label = tk.Label(root, text="Practice translating English words and progress through levels!", font=FONT_TEXT, bg=BG_COLOR, fg=FG_COLOR)
    instructions_label.pack(pady=10)

    instructions_label = tk.Label(root, text="Done by Mohammad ali ibrahim", font=FONT_TEXT, bg=BG_COLOR, fg=FG_COLOR, )
    instructions_label.pack(pady=0)
    
    start_button = tk.Button(root, text="Start", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=choose_language)
    start_button.pack(pady=20)

def choose_language():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=BG_COLOR)

    languages = ["Spanish", "French", "German", "Italian"]

    language_label = tk.Label(root, text="Choose a language to practice:", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
    language_label.pack(pady=20)

    lang_frame = tk.Frame(root, bg=BG_COLOR)
    lang_frame.pack(pady=10)

    for language_option in languages:
        lang_button = tk.Button(lang_frame, text=language_option, width=15, font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                                command=lambda lang=language_option: start_quiz(lang))
        lang_button.pack(pady=5)

def start_quiz(selected_language):
    global language, filtered_vocabulary, score, total_questions, questions_asked, level_index

    root.configure(bg=BG_COLOR)

    language = selected_language
    score = 0
    total_questions = 0
    questions_asked = []
    level_index = 0  # Start at beginner level

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
    global current_word, correct_translation, options, total_questions, level_index

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg=BG_COLOR)

    if total_questions >= (level_index + 1) * QUESTIONS_PER_LEVEL:
        # Move to the next level
        level_index += 1
        if level_index >= len(LEVELS):  # If last level is completed
            stat_result()
            return

    # Display level and XP progress
    level_label = tk.Label(root, text=f"Level: {LEVELS[level_index]} ({total_questions % QUESTIONS_PER_LEVEL + 1}/{QUESTIONS_PER_LEVEL})", font=FONT_TEXT, bg=BG_COLOR, fg=FG_COLOR)
    level_label.pack(pady=10)

    # Choose a random word that hasn't been asked yet
    current_word = random.choice(list(filtered_vocabulary.keys()))
    while current_word in questions_asked:
        current_word = random.choice(list(filtered_vocabulary.keys()))
    questions_asked.append(current_word)

    correct_translation = filtered_vocabulary[current_word][language]

    # Generate incorrect options
    all_translations = [
        v[language] for v in filtered_vocabulary.values()
        if v[language] != correct_translation
    ]

    num_options = min(3, len(all_translations))
    incorrect_options = random.sample(all_translations, num_options)

    options = incorrect_options + [correct_translation]
    random.shuffle(options)

    question_label = tk.Label(root, text=f"Translate '{current_word}' into {language}:", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
    question_label.pack(pady=20)

    user_choice = tk.StringVar()

    options_frame = tk.Frame(root, bg=BG_COLOR)
    options_frame.pack(pady=10, fill='x', expand=True)

    for option in options:
        option_button = tk.Radiobutton(options_frame, text=option, variable=user_choice, value=option, font=FONT_OPTION,
                                       bg=OPTION_COLOR, fg=FG_COLOR, selectcolor=OPTION_SELECTED_COLOR,
                                       indicatoron=0, width=20, padx=10, pady=5, relief='groove', cursor='hand2')
        option_button.pack(anchor='w', pady=5, padx=20, fill='x')

    # Display an XP-like progress bar
    progress_bar = tk.Frame(root, bg=OPTION_COLOR, height=20, width=(400 * (total_questions % QUESTIONS_PER_LEVEL + 1)) // QUESTIONS_PER_LEVEL)
    progress_bar.pack(pady=10, anchor='center')
    
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=20)

    submit_button = tk.Button(button_frame, text="Submit", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: check_answer(user_choice.get()))
    submit_button.pack(side='left', padx=10)

    stop_button = tk.Button(button_frame, text="Stop Quiz", font=FONT_BTN, bg=ERROR_COLOR, fg=BTN_TEXT_COLOR, command=confirm_stop_quiz)
    stop_button.pack(side='left', padx=10)

def confirm_stop_quiz():
    response = messagebox.askyesno("Confirm", "Are you sure you want to stop the quiz?")
    if response:
        stat_result()

def check_answer(selected_option):
    global score, total_questions

    total_questions += 1

    if selected_option == correct_translation:
        score += 1
        messagebox.showinfo("Correct!", "Your answer is correct!")

    root.configure(bg=BG_COLOR)

    result_label = tk.Label(root, text=f"You got {score} out of {total_questions} correct!", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
    result_label.pack(pady=30)

    restart_button = tk.Button(root, text="Play Again", font=FONT_BTN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=start_screen)
    restart_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=FONT_BTN, bg=ERROR_COLOR, fg=BTN_TEXT_COLOR, command=root.quit)
    exit_button.pack(pady=10)

if __name__ == "__main__":
    start_screen()
    root.mainloop()
