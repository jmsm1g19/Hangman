
# Hangman Game in Python

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Description

This project is an interactive command line Hangman game immplemented in Python. The game selects a random word from a list, and the player attempts to guess it letter by letter. The aim of this project is to demonstrate fundamental Python programming skills like control structures, data structures, and user input handling. We also explore object-oriented programming by structuring the game logic within a Python class.

Key learnings from this project include string manipulation, conditional statements, the random library in Python, and the basics of object-oriented programming. The game logic is encapsulated within a Hangman class, showcasing how classes can organize and manage game state.

## Installation

Python is required to run this project. If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

To get the game, clone this repository to your local machine using:

```bash
git clone https://github.com/jmsm1g19/hangman.git
cd hangman-game
```

## Usage

Run the game with the following command:

```bash
python hangman.py
```

Guess one letter at a time to reveal the hidden word. The game tracks your number of incorrect guesses, and you have a limited number of lives. The game ends either when you guess the word correctly or run out of lives.

## File Structure

- `hangman.py`: Contains the main Python script for the Hangman game. This script defines a Hangman class responsible for game logic and interactions.
- `README.md`: Documentation and instructions for the project.
- `LICENSE`: The license file for the project.

## License

This project is licensed under the [MIT License](LICENSE). For more details, see the LICENSE file in this repository.
