import random

# List of words to choose from
favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
word_list = favorite_fruits
word = random.choice(word_list)  # Randomly selecting a word from the list

print(word) 
guess = input("Guess a letter: ")
if len(guess) == 1 and guess.isalpha():
    # Check if the guess is in the word
    if guess in word:
        print("Good guess!")
    else:
        print("Try again!")
else:
    # Handling invalid input
    print("Oops! That is not a valid input.")
