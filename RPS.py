#Rock Paper Scissor 
import random

player_score = 0
computer_score = 0
n = int(input("Enter number of rounds: "))

def game():
    global player_score
    global computer_score
    print("ROUND", i)

    choices = ["rock", "paper", "scissor"]
    comp_choice = random.choice(choices).title()
    player_choice = str(input("Enter choice: ")).lower()

    print("Computer choice:", comp_choice)

    if ((player_choice == "rock" and comp_choice == "Paper") 
    or (player_choice == "paper" and comp_choice == "Scissor")
    or (player_choice == "scissor" and comp_choice == "Rock")):
        computer_score += 1
        print("Result: Computer wins round", i)

    elif ((comp_choice == "Rock" and player_choice == "paper") 
    or (comp_choice == "Paper" and player_choice == "scissor")
    or (comp_choice == "Scissor" and player_choice == "rock")):
        player_score += 1
        print("Result: Player wins round", i)
    else:
        print("Result: Tie")
    print("Player Score:", player_score, "\n" "Computer Score:", computer_score)
    
for i in range(1,n+1):
    game()

print("GAME OVER")
print("Player Score:", player_score, "\n" "Computer Score:", computer_score)

if player_score > computer_score:
    print("PLAYER WINS")
elif computer_score > player_score:
    print("COMPUTER WINS")
else:
    print("TIE")

