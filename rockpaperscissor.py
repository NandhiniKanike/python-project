#take input from user whether it is rock/paper/scissor
#computer choice is randomlygenerated
#and then compare the user choice and computer choice 
"""
a-rock
rock-rock-tie
rock-paper-papr win
rock-scissor-rock win

b-paper
paper-paper-tie
paper-rock-paer win
paper-scissor-scissor win

c-scissor
scissor-scissor-tie
scissor-rock-rock win
scissor-paper-scissor win
"""

import random
items=["rock","paper","scissor"]
print("Welcome to Rock-Paper-Scissor Game!!!")
while True:
    user=input("Enter your choice (Rock/Paper/Scissor):")
    comp_choice=random.choice(items)
    print(f"User choice is {user} and Computer Choice is {comp_choice}")
    if user.lower()==comp_choice.lower():
        print("You are tie")
    elif user.lower()=="rock" and comp_choice.lower()=="paper":
        print(f"Paper covers rock so Computer choice {comp_choice} wins")
    elif user.lower()=="rock" and comp_choice.lower()=="scissor":
        print(f"Rock smashes scissor so User choice {user} wins") 
    elif user.lower()=="paper" and comp_choice.lower()=="paper":
        print("You are tie")
    elif user.lower()=="paper" and comp_choice.lower()=="rock":
        print(f"Paper covers rock so User choice {user} wins")
    elif user.lower()=="paper" and comp_choice.lower()=="scissor":
        print(f" Scissor cuts the paper so Computer choice {comp_choice}wins")
    elif user.lower()=="scissor" and  comp_choice.lower()=="scissor":
        print("You are tie")
    elif user.lower()=="scissor" and comp_choice.lower()=="rock":
        print(f"Rock smashes the scissor so Computer choice {comp_choice} wins")
    elif user.lower()=="scissor" and comp_choice.lower()=="paper":
        print(f" Scissor cuts the paper so User choice {user} wins")
    else :
        print("Invalid choice,Enter the correct choice!!!")
    print("Do you want to continue(Yes/No):")
    cont=input()
    if cont.lower()=="yes":
        continue
    else :
        print("Thank you for playing Rock-Paper-Scissor Game!!!")