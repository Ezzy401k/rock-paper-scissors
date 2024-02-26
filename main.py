# import the random library to generate a random number.
import random
# accept users input.
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Set the generated number to the variable.
pc_pick = random.randint(0,2)
# If the user input is out of the given range give this error.
if user > 2:
    print("Please, input within the range!")
    pc_pick = 3
else:
    # if the user input is within the range give a corresponding sign.
    if user == 0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif user == 1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif user == 2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# if the user input is an error print this message.
if pc_pick == 3:
    print("Range 0, 1, 2")
else:
    # now the computer chooses its corresponding sign.
    print("Computer chose:")
    if pc_pick == 0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif pc_pick == 1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif pc_pick == 2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    # This code snippet is the logic of the game Rock > Scissor > Papper > Rock.
if user == 0:
    if pc_pick == 0:
        print("It's a Draw!")
    elif pc_pick == 1:
        print("You Lose!")
    elif pc_pick ==2:
        print("You Win!")
elif user == 1:
    if pc_pick == 0:
        print("You Win!")
    elif pc_pick == 1:
        print("It's a Draw!")
    elif pc_pick ==2:
        print("You Lose!")
elif user == 2:
    if pc_pick == 0:
        print("You Lose!")
    elif pc_pick == 1:
        print("You Win!")
    elif pc_pick ==2:
        print("It's a Draw!")
input("Press the Enter botton to EXIT!")
