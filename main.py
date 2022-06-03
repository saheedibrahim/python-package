import random
while True:
    myList = ["Rock", "Paper", "Scissors"]
    Player = input("Pick an option, R for Rock, P for Paper or S for Scissors: " ).upper()
    if not Player in ['R', 'P', 'S']:
        print("Invalid input" )
        continue
    CPU = random.choice(myList)
    user_option = ["R", "P", "S"]
    user_index = user_option.index(Player)
    user_option[0] = myList[0]
    user_option[1] = myList[1]
    user_option[2] = myList[2]
    user = user_option[user_index]
    if (user == "Rock" and CPU == "Scissors"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")")
        print("You Win")
        break
    elif (user == "Rock" and CPU == "Paper"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")") 
        print("The computer win")
        break
    elif (user == "Paper" and CPU == "Scissors"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")")
        print("The computer win")
        break
    elif (user == "Paper" and CPU == "Rock"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")") 
        print("You win")
        break            
    elif (user == "Scissors" and CPU == "Rock"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")")
        print("The computer win")
        break
    elif (user == "Scissors" and CPU == "Paper"):
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")") 
        print("You Win")
        break
    else:
        print("Player (" + user + ")" + " : " + "CPU (" + CPU + ")")
        print("It is a Tie pls replay: " )
