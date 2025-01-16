# Python_Developer_intern
## Task 1 Rock,paper and scissors game 

Develop a Python console-based Rock, Paper, Scissors game where players can compete against the computer. Each player selects their choice (rock, paper, or scissors), and the program determines the winner based on the classic game rules. Display the result of each round, keep track of the score, and allow players to play multiple rounds. Ensure the game handles invalid inputs and provides a user-friendly experience.

#### python - VS Code 
---

## Overview
This is a simple interactive Rock, Paper, Scissors game where the user plays against the computer. The game keeps track of the scores and continues until the user decides to quit. The program is designed to demonstrate basic programming concepts such as functions, loops, conditionals, and user interaction.

## Features
- User vs. Computer gameplay.
- The game continues until the user types "quit."
- Tracks and displays the score after each round.
- Displays the final score when the game ends.
- Easy-to-understand and beginner-friendly.

## Functions
### `get_computer_choice()`
- Purpose: Randomly generates the computer's choice from "rock", "paper", or "scissors".
- Uses the `random.choice()` method to select the computer's choice.

### `determine_winner(player_choice, computer_choice)`
- Purpose: Determines the winner of a single round based on the user's and computer's choices.
- Logic:
  - If both choices are the same, it's a draw.
  - Rock beats Scissors.
  - Scissors beats Paper.
  - Paper beats Rock.
  - Returns the winner: "player", "computer", or "draw".

### `play_game()`
- Purpose: Manages the game flow, including multiple rounds, scorekeeping, and user interaction.
- Displays a welcome message and instructions.
- Starts a loop where the user is prompted to enter their choice.
- Handles invalid input and asks the user to try again if necessary.
- Calls `get_computer_choice()` and `determine_winner()` for each round.
- Displays the current score after each round.
- Ends when the user types "quit" and displays the final score.

## Usage
1. Run the program.
2. The game will ask for your choice: "rock", "paper", or "scissors" (or "quit" to exit).
3. The computer will randomly pick a choice, and the winner of the round will be determined.
4. The current score will be displayed after each round.
5. When you're ready to quit, type "quit", and the final score will be displayed.

### Example Game Flow:
```
Welcome to Rock, Paper, Scissors!
Type 'rock', 'paper', 'scissors', or 'quit' to exit the game.

Your choice: rock
Computer's choice: scissors
You win! Your score: 1 | Computer's score: 0

Your choice: paper
Computer's choice: rock
You win! Your score: 2 | Computer's score: 0

Your choice: quit
Final Score - You: 2 | Computer: 0
Thanks for playing!
```

## Notes
- Ensure you enter valid choices (rock, paper, or scissors). If an invalid choice is entered, the game will prompt you to try again.
- The program will display the final score only when you quit.

## License
This project is open-source and available for personal use and learning purposes.
