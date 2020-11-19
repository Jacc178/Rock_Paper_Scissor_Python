#Rock Paper Scissor 
import random

#main function, initially called once, recalled if player choses to play again
def play():
    #Declaring variables to store user and computer score, number of rounds 

    player_score = 0
    computer_score = 0
    n = int(input("Enter number of rounds: "))

    #nested function, controls one round of the game
    def game():
        # nonlocal used to make score variables declared in containing function accessible is nested function

        nonlocal player_score
        nonlocal computer_score
        print("\nROUND", i, "\n")

        #computer choice randomly generated using random.choice with a list containing all possible choices passed as the argument, converted to title case
        #player choice taken as input, converted to lower case using lower() (to make program case insensitive)
        choices = ["rock", "paper", "scissor"]
        comp_choice = random.choice(choices).title()
        player_choice = str(input("Enter choice: ")).lower()

        print("Computer choice:", comp_choice)

        #if statement checks if computer wins the round, increments computer score variable by 1 if true
        if ((player_choice == "rock" and comp_choice == "Paper") 
        or (player_choice == "paper" and comp_choice == "Scissor")
        or (player_choice == "scissor" and comp_choice == "Rock")):
            computer_score += 1
            print("\nResult: Computer wins round", i, "\n")

        #elif statement checks if player wins the round, increments player score variable by 1 if true
        elif ((comp_choice == "Rock" and player_choice == "paper") 
        or (comp_choice == "Paper" and player_choice == "scissor")
        or (comp_choice == "Scissor" and player_choice == "rock")):
            player_score += 1
            print("\nResult: Player wins round", i, "\n")

        #second elif statement evaluates to true if player enters something other than rock, paper or scissor. Recalls game() function to resume game from i'th round.
        elif player_choice not in choices:
            print("Invalid Input. Enter rock, paper or scissor")
            game()

        #else is true if player and computer pick the same choice, round ties, scores remain unchanged    
        else:
            print("Result: Tie")
        print("Player Score:", player_score, "\n" "Computer Score:", computer_score)

    #second nested function, prints results of the game after n rounds are over. n -> variable that stores number of rounds
    def results():
        print("\n\nGAME OVER")
        print("Player Score:", player_score, "\n" "Computer Score:", computer_score)

        if player_score > computer_score:
            print("\nPLAYER WINS")
        elif computer_score > player_score:
            print("\nCOMPUTER WINS")
        else:
            print("\nTIE")
    
    #for loop to call game() function n times to play a game of n rounds
    for i in range(1,n+1):
        game()
    results()

play()

#replay takes user input to determine whether program runs again to play another game, or exit
replay = input("Play Again? (Y/N): ").upper()
if replay == "Y":
    play()
else:
    print("\nThanks for playing")
