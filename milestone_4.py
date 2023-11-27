import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def update_game_state(self, guess):
        """
        Update the game state when a correct guess is made.
        """
        new_guess = guess not in self.list_of_guesses
        self.list_of_guesses.append(guess)

        if new_guess:
            self.num_letters -= 1
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_game_state(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while self.num_lives > 0 and '_' in self.word_guessed:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                print("Word guessed so far:", ' '.join(self.word_guessed))

        self.end_game()

    def end_game(self):
        if '_' not in self.word_guessed:
            print("Congratulations! You guessed the word:", self.word)
        else:
            print("Game over! The word was:", self.word)

# Example usage
favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
game = Hangman(favorite_fruits)
game.ask_for_input()
