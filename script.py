player_wins = 0
computer_wins = 0

import random

while player_wins < 2 and computer_wins < 2:
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)

  print("Let's play rock, paper, or scissors")
  player_choice = input("Rock/Paper/Scissors? ").lower()

  print(f"Computer chose: {computer_choice}")

  winner = ""
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif (player_choice == computer_choice):
    winner = "Tie"
  else:
    winner = "Computer"

  if winner == "Player":
    print("You won")
    player_wins += 1
  elif winner == "Computer":
    print("Computer won")
    computer_wins += 1
  else:
    print("It's a tie")
  
  print(f"Current score - Player: {player_wins}, Computer: {computer_wins}")

if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
  print("Computer won!")