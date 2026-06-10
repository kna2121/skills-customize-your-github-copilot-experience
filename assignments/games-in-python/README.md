
# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses strings, loops, and user input to let a player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Create the game loop

#### Description
Write the main game loop that prompts the player for letter guesses, updates the current word display, and tracks which letters have been guessed.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list
- Accept a single letter guess from the player each turn
- Show the current word state with unguessed letters as underscores
- Track and display all guessed letters

### 🛠️ Handle win/lose conditions

#### Description
Implement logic to determine when the player has won or lost, and show the appropriate result message.

#### Requirements
Completed program should:

- Count remaining incorrect guesses and stop the game when attempts run out
- End the game when the player guesses the entire word
- Display a win message if the word is guessed
- Display a lose message if the player runs out of attempts
