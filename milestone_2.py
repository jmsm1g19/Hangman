import random

favorite_fruits = ['apple', 'banana', 'cherry', 'plum', 'grape']
word_list = favorite_fruits
word = random.choice(word_list)

print(word) 
guess = input("Guess a letter: ")
if len(guess) == 1 and guess.isalpha():
    if guess in word:
        print("Good guess!")
    else:
        print("Try again!")
else:
    print("Oops! That is not a valid input.")
