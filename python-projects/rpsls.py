# Rock Paper Scissors Lizard Spock
# 4/6/2023
import random

print("""
Enter your choice! (1-5)
1. Rock
2. Paper
3. Scissors
4. Lizard
5. Spock
""")
user = int(input())

comp = random.randint(1,5)
if comp == 1:
    compt = 'Rock'
elif comp == 2:
    compt = 'Paper'
elif comp == 3:
    compt = 'Scissors'
elif comp == 4:
    compt = 'Lizard'
else:
    compt = 'Spock'

if user == comp:
    print("Its a tie!")

# User wins
elif user == 1 and (comp == 3 or comp == 4):
    print(f"The computer chose {compt}, you win!")
elif user == 2 and (comp == 1 or comp == 5):
    print(f"The computer chose {compt}, you win!")
elif user == 3 and (comp == 2 or comp == 4):
    print(f"The computer chose {compt}, you win!")
elif user == 4 and (comp == 2 or comp == 5):
    print(f"The computer chose {compt}, you win!")
elif user == 5 and (comp == 1 or comp == 3):
    print(f"The computer chose {compt}, you win!")

# User loses
elif comp == 1 and (user == 3 or user == 4):
    print(f"The computer chose {compt}, you lose!")
elif comp == 2 and (user == 1 or user == 5):
    print(f"The computer chose {compt}, you lose!")
elif comp == 3 and (user == 2 or user == 4):
    print(f"The computer chose {compt}, you lose!")
elif comp == 4 and (user == 2 or user == 5):
    print(f"The computer chose {compt}, you lose!")
elif comp == 5 and (user == 1 or user == 3):
    print(f"The computer chose {compt}, you lose!")
