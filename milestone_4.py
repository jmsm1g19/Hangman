import random

favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
word_list = favorite_fruits
word = random.choice(word_list)

print(word)  # You might want to remove this line in the final version to keep the word a secret

guess = input("Guess a letter: ") # get a letter from the player

# Step 1: Check if the guess is of length 1 and is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement
    if guess in word:
        print("Good guess!")
    else:
        print("Try again!")
else:
    # Step 3: Else block for invalid input
    print("Oops! That is not a valid input.")
