import random

mycomputerOption = ["Rock", "Paper", "Scissors"]
yourOption = input("Pick between R for Rock, P for Paper or S for Scissors: " ).upper()
while yourOption not in ['R', 'P', 'S']:
    yourOption = input("Invalid input please pick between R, P or S: " ).upper()

else:
    computerOption = random.choice(mycomputerOption)

    if (yourOption == "R" and computerOption == "Rock"):
        print("Computer option is: " + computerOption )
        print("It is a Tie")
    elif (yourOption == "R" and computerOption == "Scissors"):
        print("Computer option is: " + computerOption ) 
        print("You Win")
    elif (yourOption == "R" and computerOption == "Paper"):
        print("Computer option is: " + computerOption )   
        print("The computer win")
    elif (yourOption == "P" and computerOption == "Rock"):
        print("Computer option is: " + computerOption )    
        print("Win")
    elif (yourOption == "P" and computerOption == "Scissors"):
        print("Computer option is: " + computerOption )   
        print("Lose")
    elif (yourOption == "P" and computerOption == "Paper"):
        print("Computer option is: " + computerOption )    
        print("Tie")
    elif (yourOption == "S" and computerOption == "Rock"):
        print("Computer option is: " + computerOption )   
        print("Lose")
    elif (yourOption == "S" and computerOption == "Scissors"):
        print("Computer option is: " + computerOption )    
        print("Tie")
    else:
        (yourOption == "S" and computerOption == "Paper")
        print("Computer option is: " + computerOption )  
        print("Win")