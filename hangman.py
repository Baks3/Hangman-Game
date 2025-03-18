import random
import threading
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

    selected_category = random.choice(list(categories.keys()))
    print(f"Your category is: {selected_category}")
    word = random.choice(categories[selected_category]).lower()
    
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = []
    score = 0
    hints = 1

    print(f"Your category is: {selected_category}")
    print(f"The word has {len(word)} letters")

    def timed_input(prompt, timeout=10):
        result = [None]

        def get_input():
            result[0] = input(prompt)

        t = threading.Thread(target=get_input)
        t.daemon = True
        t.start()
        t.join(timeout)

        if t.is_alive():
            print(Fore.RED + "\n⏰ Time's up!")
            return None
        return result[0]

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

    while True:
        main = ""
        for letter in word:
            if letter in guessmade:
                main += letter + " "
            else:
                main += "_ "

        print("\nGuess the word:", main.strip())

        if main.replace(" ", "") == word:
            print(Fore.GREEN + f"🎉 Congratulations! You won with {score} points!")
            break

        if hints > 0:
            hint = input(Fore.YELLOW + "Do you need a hint? (yes/no): ").lower()
            if hint == "yes":
                print(Fore.YELLOW + f"Hint: The first letter is '{word[0]}'")
                hints -= 1

        guess = timed_input(Fore.CYAN + "Enter a letter (10 sec): ", timeout=10)
        if guess is None:
            turns -= 1
            score -= 5
            print(Fore.RED + f"❌ No input - You lost a turn! Turns left: {turns}")
        else:
            guess = guess.lower()
            if len(guess) != 1 or guess not in valid_letters:
                print(Fore.RED + "⚠️ Invalid input. Please enter a single valid letter.")
                continue

            if guess in guessmade:
                print(Fore.YELLOW + "⚠️ You already guessed that letter.")
                continue

            guessmade.append(guess)

            if guess in word:
                print(Fore.GREEN + "✅ Correct Guess!")
                score += 10
            else:
                print(Fore.RED + "❌ Wrong Guess!")
                turns -= 1
                print(f"{turns} turns left")
                score -= 5

        if turns <= len(stages) and turns > 0:
            print(stages[10 - turns])

        if turns == 0:
            print(Fore.RED + f"\n💀 You lost! The word was: {word}")
            break

    replay = input(Fore.CYAN + "Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        hangman()
    else:
        print(Fore.CYAN + "Thank you for playing! Goodbye!")
