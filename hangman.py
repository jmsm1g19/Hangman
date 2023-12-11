import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with a randomly selected word from the word_list.
        Args:
            word_list (list): List of words to choose from.
            num_lives (int, optional): Number of lives the player starts with. Defaults to 5.
        """
        self.word = random.choice(word_list)  # Randomly chosen word from the list
        self.word_guessed = ['_' for _ in self.word]  # List of underscores representing unguessed letters
        self.num_letters = len(set(self.word))  # Unique letters in the word
        self.num_lives = num_lives  # Initial number of lives
        self.list_of_guesses = []  # An empty list to keep track of guesses

    def update_game_state(self, guess):
        """
        When a guess is made, update the game state.
        If the guess is new and correct, update the word_guessed list and decrease num_letters.
        Args:
            guess (str): The letter guessed by the player.
        """
        is_new_guess = guess not in self.list_of_guesses
        self.list_of_guesses.append(guess)

        if is_new_guess and guess in self.word:
            self.num_letters -= 1
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        Updates the game state and number of lives based on the guess's correctness.
        Args:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_game_state(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")


    def ask_for_input(self):
        """
        Repeatedly ask the player to guess a letter until the game ends.
        Validate the input and provides feedback based on the guess.
        """
        while self.num_lives > 0 and '_' in self.word_guessed:
            guess = input("Guess a letter: ").lower()
    
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                print("Word guessed so far:", ' '.join(self.word_guessed))

    def end_game(self):
        """
        End the game by either congratulating the player or revealing the word.
        The game ends when the player runs out of lives or guesses the word.
        """
        if '_' not in self.word_guessed:
            print("Congratulations! You guessed the word:", self.word)
        elif self.num_lives == 0:
            print("Game over! The word was:", self.word)


def play_game(word_list):
    """
    Start a game of Hangman.
    Creates a Hangman instance and runs the game loop.
    Args:
        word_list (list): List of words to choose from for the Hangman game.
    """
    game = Hangman(word_list, num_lives=5)

    while game.num_lives > 0 and '_' in game.word_guessed:
        game.ask_for_input()

    game.end_game()


favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
play_game(favorite_fruits)