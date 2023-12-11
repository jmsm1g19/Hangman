import random

# Selecting a random word from the list
favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
word = random.choice(favorite_fruits)
print('Word: ', word)

def check_guess(guess):
    """
    Check if the guessed letter is in the word and print appropriate feedback.
    Args:
        guess (str): The letter guessed by the player.
    """
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """
    Prompt the player for a letter and validate the input.
    Repeats until a valid letter is entered.
    """
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break 
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()
