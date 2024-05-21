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

rps_list = [rock, paper, scissors]

user_choose = int(input("Choose rock(1), paper(2), OR scissors(3)! "))
final_user = user_choose - 1
computer_choose = random.randint(0, 2)

if final_user >= 4 or final_user < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(rps_list[final_user])
  print(rps_list[computer_choose])
  if final_user == 0 and computer_choose == 2:
   print("You win!")
  elif computer_choose == 0 and final_user == 2:
   print("You lose")
  elif computer_choose > final_user:
   print("You lose")
  elif final_user > computer_choose:
   print("You win!")
  elif computer_choose == final_user:
   print("It's a draw")

