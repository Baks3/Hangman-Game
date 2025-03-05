import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def hangman():
    categories = {
        "Superheroes": ['superman', 'batman', 'spiderman', 'thor', 'ironman'],
        "Animals": ['elephant', 'giraffe', 'kangaroo', 'dolphin', 'penguin'],
        "Countries": ['southafrica', 'america', 'nigeria', 'canada', 'germany'],
        "Food": ['pizza', 'hamburger', 'spaghetti', 'sandwich', 'biryani']
    }

    print("Choose a category:")
    for i, category in enumerate(categories.keys(), start=1):
        print(f"{i}. {category}")

    choice = int(input("Enter your choice (1-4): "))
    selected_category = list(categories.keys())[choice - 1]
    word = random.choice(categories[selected_category]).lower()
    
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = []
    score = 0

    print(f"The word has {len(word)} letters")

    while True:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main += letter + " "
            else:
                main += "_ "

        print("\nGuess the word:", main.strip())

        if main.replace(" ", "") == word:
            print(Fore.GREEN + f"🎉 Congratulations! You won with {score} points!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess not in valid_letters:
            print(Fore.RED + "⚠️ Invalid input. Please enter a single letter.")
            continue

        if guess in guessmade:
            print(Fore.YELLOW + "⚠️ You already guessed that letter.")
            continue

        guessmade.append(guess)

        if guess in word:
            print(Fore.GREEN + "✅ Correct Guess!")
        else:
            print(Fore.RED + "❌ Wrong Guess!")
            turns -= 1
            print(f"{turns} turns left")

        stages = [
            "  --------  \n     O_|    \n    /|\\      \n    / \\     ",
            "  --------  \n   \\ O_|/   \n     |      \n    / \\     ",
            "  --------  \n   \\ O /|   \n     |      \n    / \\     ",
            "  --------  \n   \\ O /    \n     |      \n    / \\     ",
            "  --------  \n   \\ O      \n     |      \n    / \\     ",
            "  --------  \n     O      \n     |      \n    / \\     ",
            "  --------  \n     O      \n     |      \n    /       ",
            "  --------  \n     O      \n     |      ",
            "  --------  \n     O      ",
            "  --------  "
        ]

        if turns < len(stages):
            if turns > 0:
                print(stages[turns - 10])
            else:
                print(stages[0]) 


        if turns == 0:
            print(Fore.RED + f"\n💀 You lost! The word was: {word}")
            break

    print(Fore.CYAN + "Thank you for playing! Goodbye!")

