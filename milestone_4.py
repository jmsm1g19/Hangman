import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        """
        Prompt the user for a letter and validate the input.
        """
        while True:
            guess = input("Guess a letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
game = Hangman(favorite_fruits)
game.ask_for_input()
