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
        Check if the guessed letter is in the word and update the game state accordingly.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            # Check if the guess is a new correct guess
            if guess not in self.word_guessed:
                self.num_letters -= 1  # Decrease the number of unique letters left to guess

            # Replace the underscores with the correctly guessed letter
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
        else:
            # Handling incorrect guesses
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

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
                # Display the current state of the guessed word
                print("Word guessed so far:", ' '.join(self.word_guessed))
                if '_' not in self.word_guessed or self.num_lives <= 0:
                    break  # Exit the loop if the game is over

        # Check for win or lose
        if '_' not in self.word_guessed:
            print("Congratulations! You guessed the word:", self.word)
        else:
            print("Game over! The word was:", self.word)

# Example usage
favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
game = Hangman(favorite_fruits)
game.ask_for_input()
