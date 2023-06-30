

import random

active = True
player_wins = 0
computer_wins = 0


def determine_winner(player_choice, computer_choice):
    global player_wins, computer_wins

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        player_wins += 1
        return "You win!"
    else:
        computer_wins += 1
        return "Computer wins!"


def play_game():
    global active

    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Stone, Paper, Scissors!")
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    player_choice = int(input("Enter your choice (1-4): ")) - 1

    if player_choice == 3:
        active = False
        return

    if player_choice < 0 or player_choice >= 4:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.choice(choices)

    player_choice_text = choices[player_choice]

    print("You chose:", player_choice_text)
    print("Computer chose:", computer_choice)

    result = determine_winner(player_choice_text, computer_choice)
    print(result)
    print("Player wins:", player_wins)
    print("Computer wins:", computer_wins)


while active:
    play_game()

print("You have successfully quit the game")
