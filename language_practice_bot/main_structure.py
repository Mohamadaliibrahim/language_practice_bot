import random
import json

def language_practice_bot():
    # Load the vocabulary outside the loop, only once
    with open('vocabulary.json', 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    print("Welcome to the Language Practice Bot!")
    print("You can practice translating English words into another language.")

    languages = ["Spanish", "French"]
    print("Available languages:", ", ".join(languages))
    language = input("Please choose a language to practice: ").capitalize()

    if language not in languages:
        print("Sorry, that language is not available.")
        return

    score = 0
    total_questions = 0

    while True:
        total_questions += 1
        word = random.choice(list(vocabulary.keys()))
        correct_translation = vocabulary[word][language]

        # Generate incorrect options
        all_translations = [v[language] for v in vocabulary.values() if v[language] != correct_translation]
        
        # Ensure there are enough translations to sample from
        num_options = min(3, len(all_translations))
        incorrect_options = random.sample(all_translations, num_options)

        # Combine correct and incorrect translations and shuffle
        options = incorrect_options + [correct_translation]
        random.shuffle(options)

        print(f"\nTranslate '{word}' into {language}:")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        user_choice = input("Your answer (enter the number): ").strip()

        # Validate user input
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(options):
            if options[int(user_choice) - 1] == correct_translation:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct translation is '{correct_translation}'.")
        else:
            print(f"Invalid input. Please enter a number between 1 and {len(options)}.")

        continue_prompt = input("Do you want to try another word? (y/n): ").strip().lower()
        if continue_prompt != "y":
            break

    print(f"\nYou got {score} out of {total_questions} correct. Thank you for practicing!")

if __name__ == "__main__":
    language_practice_bot()
