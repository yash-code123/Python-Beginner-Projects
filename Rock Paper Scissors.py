import random

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
game_icon = [rock, paper, scissors]
user_choice = int(input("What do to want to choose (0 rock, 1 paper or 2 scissors): "))

if user_choice >= 0 and user_choice <= 2:
    print(game_icon[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_icon[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("invalid input")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 0 and  computer_choice == 1:
    print("You Lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
elif user_choice == computer_choice:
    print("Match draw!")
