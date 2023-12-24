rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
list1 =[rock, paper, scissors]
a = input("What do you want to choose? Type '0' for rock '1' for paper and '2' for scissors.\n")
if a == "0":
    print(rock)
    computer_choice = random.choice(list1)
    if computer_choice == scissors:
        print("you won as the computer choose:\n",computer_choice)
    elif computer_choice == paper:
        print("you lose as the computer choose:\n",computer_choice)    
    elif computer_choice == rock:
        print("its a tie as the computer choose:\n",computer_choice)
elif a == "1":
    print(paper)
    computer_choice = random.choice(list1)
    if computer_choice == rock:
        print("you won as the computer choose:\n",computer_choice)
    elif computer_choice == scissors:
        print("you lose as the computer choose:\n",computer_choice)
    elif computer_choice == paper:
        print("it's a tie as the computer choose:\n",computer_choice)
elif a =="2":
    print(scissors)
    computer_choice = random.choice(list1)
    if computer_choice == rock:
        print("you lose as the computer choose:\n",computer_choice)
    elif computer_choice == paper:
        print("you won as the computer choose:\n",computer_choice)
    elif computer_choice == scissors:
        print("it's a tie as the computer choose:\n",computer_choice)

