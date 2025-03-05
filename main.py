import hangman
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def main():
    print(Fore.CYAN + "Welcome to Hangman Game!")
    print("----------------------------")
    name = input("Enter your name: ")
    print(f"Hello {name}!")
    print("Try to guess the word in less than 10 attempts.")
    hangman.hangman()

if __name__ == "__main__":
    main()