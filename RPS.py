#Rock Paper Scissor 
import random
def play():
    player_score = 0
    computer_score = 0
    n = int(input("Enter number of rounds: "))

    def game():
        nonlocal player_score
        nonlocal computer_score
        print("\nROUND", i, "\n")

        choices = ["rock", "paper", "scissor"]
        comp_choice = random.choice(choices).title()
        player_choice = str(input("Enter choice: ")).lower()

        print("Computer choice:", comp_choice)

        if ((player_choice == "rock" and comp_choice == "Paper") 
        or (player_choice == "paper" and comp_choice == "Scissor")
        or (player_choice == "scissor" and comp_choice == "Rock")):
            computer_score += 1
            print("\nResult: Computer wins round", i, "\n")

        elif ((comp_choice == "Rock" and player_choice == "paper") 
        or (comp_choice == "Paper" and player_choice == "scissor")
        or (comp_choice == "Scissor" and player_choice == "rock")):
            player_score += 1
            print("\nResult: Player wins round", i, "\n")
        else:
            print("Result: Tie")
        print("Player Score:", player_score, "\n" "Computer Score:", computer_score)

    def results():
        print("\n\nGAME OVER")
        print("Player Score:", player_score, "\n" "Computer Score:", computer_score)

        if player_score > computer_score:
            print("\nPLAYER WINS")
        elif computer_score > player_score:
            print("\nCOMPUTER WINS")
        else:
            print("\nTIE")

    for i in range(1,n+1):
        game()
    results()

play()

replay = input("Play Again? (Y/N): ").upper()
if replay == "Y":
    play()
else:
    print("\nThanks for playing")
