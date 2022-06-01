import random
myList = ["Rock", "Paper", "Scissors"]
Player = input("Pick between R for Rock, P for Paper or S for Scissors: " ).upper()
while Player not in ['R', 'P', 'S']:
    Player = input("Invalid input please pick between R, P or S: " ).upper()
else:    
    CPU = random.choice(myList)
    while ((Player == "R" and CPU == "Rock") or (Player == "S" and CPU == "Scissors") or (Player == "P" and CPU == "Paper")):
            print("Player (" + Player + ")" + " : " + "CPU (" + CPU + ")")
            Player = input("It is a Tie pls replay: " ).upper()
    else:
        if (Player == "R" and CPU == "Scissors"):
            print("Player (Rock)" + " : " +  "CPU (" + CPU + ")")
            print("You Win")
        elif (Player == "R" and CPU == "Paper"):
            print("Player (Rock)" + " : " +  "CPU (" + CPU + ")")   
            print("The computer win")
        if (Player == "P" and CPU == "Scissors"):
            print("Player (Paper)" + " : " +  "CPU (" + CPU + ")")
            print("The computer win")
        elif (Player == "P" and CPU == "Rock"):
            print("Player (Paper)" + " : " +  "CPU (" + CPU + ")")   
            print("You win")
        if (Player == "S" and CPU == "Rock"):
            print("Player (Scissors)" + " : " +  "CPU (" + CPU + ")")
            print("The computer win")
        elif (Player == "S" and CPU == "Paper"):
            print("Player (Scissors)" + " : " +  "CPU (" + CPU + ")")   
            print("You Win")