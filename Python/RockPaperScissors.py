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
import random
game = [rock,paper,scissors]
game_num = random.randint(0,2)
Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if Choice == 0:
    print(rock)
elif Choice == 1:
    print(paper)
elif Choice == 2:
    print(scissors)
else:
    print("You typed an invalid number")

print(game[game_num])
if Choice == 0 and game_num == 0:
    print("It's a draw")
if Choice == 0 and game_num == 1:
    print("You lose")
if Choice == 0 and game_num == 2:
    print("You win")
if Choice == 1 and game_num == 0:
    print("You win")
if Choice == 1 and game_num == 1:
    print("It's a draw")
if Choice == 1 and game_num == 2:
    print("You lose")
if Choice == 2 and game_num == 0:
    print("You lose")
if Choice == 2 and game_num == 1:
    print("You win")
if Choice == 2 and game_num == 2:
    print("It's a draw")
