from ast import alias
import random

myList = ["Rock", "Paper", "Scissors"]
Player = input("Pick between R for Rock, P for Paper or S for Scissors: " ).upper()
while Player not in ['R', 'P', 'S']:
    Player = input("Invalid input please pick between R, P or S: " ).upper()

else:
    # R = myList[0]
    # P = myList[1]
    # S = myList[2]
    alias 'R' is 'Rock'
    'Paper' is 'P'
    'Scisors' is 'R'
    CPU = random.choice(myList)
    # "R" as Rock
    # if (Player == "R"):
    #     Rock = Player
    # elif (Player == "S"):
    #     Scissors = Player
    # else:
    #     Paper = Player
    if Player == CPU:
        print(Player, CPU)
        print("it is a tie")

        # if ((Player == Rock and CPU == R) or (Player == Scissors and CPU == S) or (Player == Paper and CPU == P)):
            # print("It is a tie")
            # print(Player, CPU)
    #     R = Player
    # if Player == "P":
    #     R = Player
    # if Player == "R":
    #     R = Player
    # while (Player == CPU):
    #     print("Tie")

# print(R)

    # while 
    # (Player == "R" and CPU == "Rock"):
    #     print("Player " + "(Rock)" + " : " + "CPU" + "(Rock)")
    #     # print("Computer option is: " + CPU )
    #     print("It is a Tie")
    # elif (Player == "R" and CPU == "Scissors"):
    #     print("Computer option is: " + CPU ) 
    #     print("You Win")
    # elif (Player == "R" and CPU == "Paper"):
    #     print("Computer option is: " + CPU )   
    #     print("The computer win")
    # elif (Player == "P" and CPU == "Rock"):
    #     print("Computer option is: " + CPU )    
    #     print("You Win")
    # elif (Player == "P" and CPU == "Scissors"):
    #     print("Computer option is: " + CPU )   
    #     print("The computer win")
    # elif (Player == "P" and CPU == "Paper"):
    #     print("Computer option is: " + CPU )    
    #     print("It is a Tie")
    # elif (Player == "S" and CPU == "Rock"):
    #     print("Computer option is: " + CPU )   
    #     print("The computer win")
    # elif (Player == "S" and CPU == "Scissors"):
    #     print("Computer option is: " + CPU )    
    #     print("It is a Tie")
    # else:
    #     (Player == "S" and CPU == "Paper")
    #     print("Computer option is: " + CPU )  
    #     print("Win")