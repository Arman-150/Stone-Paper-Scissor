import random

print("Welcome to (Stone, Paper, Scissors)")
Player = input("Enter Your Name:- ")
Computer = random.choice([1, 0, -1])



gesturestr = input("Enter your gesture, Stone, Paper, Scissors:- ").capitalize()
compDict = {"Stone": 1, "Paper": 0, "Scissors": -1}
reverseDict = {1: "Stone", 0: "Paper", -1: "Scissors"}



if gesturestr not in compDict:
    print("PLease select a right gesture:- Stone, Paper, Scissors")
else:
    Player_gesture = compDict[gesturestr]
    if Computer == Player_gesture:
        print(f"Computer Choose, {reverseDict[Computer]} \n {Player} Choose {reverseDict[Player_gesture]} It's a Draw")
    else:
        if Computer == 1 and Player_gesture == 0:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Player Wins")
        elif Computer == 1 and Player_gesture == -1:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Computer Wins")
        elif Computer == 0 and Player_gesture == 1:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Computer Wins")
        elif Computer == 0 and Player_gesture == -1:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Player Wins")
        elif Computer == -1 and Player_gesture == 1:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Player Wins")
        elif Computer == -1 and Player_gesture == 0:
            print(f"Computer choose {reverseDict[Computer]} \n {Player} choose {reverseDict[Player_gesture]} Computer Wins")


