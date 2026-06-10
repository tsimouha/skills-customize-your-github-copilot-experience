# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game using Python strings, loops, conditionals, and user input. Practice managing game state, validating guesses, and displaying progress to the player.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a list of possible words and initialize the Hangman game state before the first guess.

#### Requirements
Completed program should:

- Define a predefined list of words.
- Randomly select one word each time the game starts.
- Initialize the guessed letters, remaining attempts, and the hidden progress display.

### 🛠️ Letter Guessing and Progress Display

#### Description
Prompt the player for letter guesses and update the displayed word progress after each valid guess.

#### Requirements
Completed program should:

- Accept a single letter guess from the user.
- Reveal correctly guessed letters in the progress display (for example: `_ _ a _ _`).
- Track incorrect guesses and decrement remaining attempts appropriately.
- Avoid counting duplicate guesses more than once.

### 🛠️ Win/Lose Messages

#### Description
Detect when the game ends and show a clear win or lose message.

#### Requirements
Completed program should:

- End the game when the player guesses the entire word or runs out of attempts.
- Display a win message if the word is guessed.
- Display a lose message with the correct word when attempts are exhausted.
