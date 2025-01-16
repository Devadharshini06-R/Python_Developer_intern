import random
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)
def determine_winner(Player,Computer):
    if Player == Computer:
        return "draw"
    elif (Player  == "rock" and Computer == "scissors") or \
         (Player == "scissors" and Computer == "paper") or \
         (Player == "paper" and Computer == "rock"):
        return "Player"
    else:
        return "Computer"
def play_game():
    print("WELCOME TO rock, paper, scissors!")
    print("TYPE 'quit' TO END THE GAME.")
    Player_score = 0
    Computer_score = 0
    while True:
        print("\n ---NEW ROUND---")
        Player_choice = input ("ENTER YOUR CHOICE (rock, paper, scissors):").lower()
        if Player_choice == "quit":
            break
        if Player_choice not in ["rock","paper","scissors"]:
            print("Invalid input. Please try again.")
            continue
        Computer_choice = get_computer_choice()
        print(f"Computer chose:{Computer_choice}")
        result = determine_winner(Player_choice,Computer_choice)
        if result == "draw":
            print("IT'S A DRAW")
        elif result == "Player":
            print("Player WINS THIS ROUND!")
            Player_score += 1
        else:
            print("COMPUTER WINS THIS ROUND!")
            Computer_score += 1
        print(f"SCORE: you {Player_score} - {Computer_score} Computer")
        print(f"\n FINAL SCORE : you {Player_score} - {Computer_score} Computer") 
        print("GOODBYE!")
if __name__ == "__main__":
    play_game()   

                                    

