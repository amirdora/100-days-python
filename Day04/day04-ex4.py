import random

# Rock paper scissor game 

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

userOption = int(input("Please choose your option: 0. Rock 1. Paper 2. Scissors: "))

computerSelection = random.randint(0,2)

print(f"Computer selection: {computerSelection}")

if userOption == 0 and computerSelection == 2:
    print(rock)
    print("You win!")

elif userOption == 1 and computerSelection == 0:
    print(paper)
    print("You win!")

elif userOption == 2 and computerSelection == 1:
    print(scissors)
    print("You win!")

elif (userOption == 0 and computerSelection == 0) or (userOption == 1 and computerSelection == 1) or (userOption == 2 and computerSelection == 2):
    print("It's a draw!")

elif userOption != 0 and userOption != 1 and userOption != 2: 
    print("Please enter a valid option.")

else:
    print("you lose!")

