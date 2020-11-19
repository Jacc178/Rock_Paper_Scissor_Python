#Rock Paper Scissor
import random

#main function, initially called once, recalled if player choses to play again
def play():
    #Declaring variables to store user and computer score, number of rounds 
    playerScore = 0
    computerScore = 0
    n = int(input("Enter number of rounds: "))

    #nested function, controls one round of the game
    def game():
        # nonlocal used to make score variables declared in containing function accessible is nested function

        nonlocal playerScore
        nonlocal computerScore
        print("\nROUND", i, "\n")

        #computer choice randomly generated using random.choice with a list containing all possible choices passed as the argument, converted to title case
        #player choice taken as input, converted to lower case using lower() (to make program case insensitive)
        choices = ["rock", "paper", "scissor"]
        computerChoice = random.choice(choices).title()
        playerChoice = str(input("Enter choice: ")).lower()

        print("Computer choice:", computerChoice)

        #if statement checks if computer wins the round, increments computer score variable by 1 if true
        if ((playerChoice == "rock" and computerChoice == "Paper") 
        or (playerChoice == "paper" and computerChoice == "Scissor")
        or (playerChoice == "scissor" and computerChoice == "Rock")):
            computerScore += 1
            print("\nResult: Computer wins round", i, "\n")

        #elif statement checks if player wins the round, increments player score variable by 1 if true
        elif ((computerChoice == "Rock" and playerChoice == "paper") 
        or (computerChoice == "Paper" and playerChoice == "scissor")
        or (computerChoice == "Scissor" and playerChoice == "rock")):
            playerScore += 1
            print("\nResult: Player wins round", i, "\n")

        #second elif statement evaluates to true if player enters something other than rock, paper or scissor. Recalls game() function to resume game from i'th round.
        elif playerChoice not in choices:
            print("Invalid Input. Enter rock, paper or scissor")
            game()

        #else is true if player and computer pick the same choice, round ties, scores remain unchanged    
        else:
            print("Result: Tie")
        print("Player Score:", playerScore, "\n" "Computer Score:", computerScore)

    #second nested function, prints results of the game after n rounds are over. n -> variable that stores number of rounds
    def results():
        print("\n\nGAME OVER")
        print("Player Score:", playerScore, "\n" "Computer Score:", computerScore)

        if playerScore > computerScore:
            print("\nPLAYER WINS")
        elif computerScore > playerScore:
            print("\nCOMPUTER WINS")
        else:
            print("\nTIE")
    
    #for loop to call game() function n times to play a game of n rounds
    for i in range(1,n+1):
        game()
    results()

play()

#declaring variable to set up while loop which repeats if player enters y to play again. If player enters n, condition (variable playAgain) becomes false, loop stops
playAgain = True
while playAgain:
    replay = input("\nPlay Again? (Y/N): ").upper()

    if replay == "Y":
        print("\nNEW GAME \n")
        play()
    else:
        playAgain = False
        print("\nThanks for playing")
