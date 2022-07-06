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
users_choice=input("choise rock paper or scissors. type \nR-rock\nP-paper\nS-scissors\n")
users_choice=users_choice.lower()
if users_choice=="s":
  print(f"you choose\n{scissors}")
elif users_choice=="p":
  print(f"you choose\n{paper}")
elif users_choice=="r":
  print(f"you choose\n{rock}")
choice=random.choice(['paper','scissors', 'rock'])
if choice=="scissors":
  print(f"computer chooses\n{scissors}")
elif choice=="paper":
  print(f"computer chooses\n{paper}")
elif choice=="rock":
  print(f"computer chooses\n{rock}")

if users_choice=='p'and choice=='scissors':
  print("you lose")
elif users_choice=='p'and choice=='rock':
  print("you win")
elif users_choice=='p'and choice=='paper':
  print("draw")
elif users_choice=='s'and choice=='scissors':
  print("its draw")
elif users_choice=='s'and choice=='rock':
  print("you lost")
elif users_choice=='s'and choice=='paper':
  print("you win")
if users_choice=='r'and choice=='scissors':
  print("you win")
elif users_choice=='r'and choice=='rock':
  print("its a draw")
elif users_choice=='r'and choice=='paper':
  print("you lost")