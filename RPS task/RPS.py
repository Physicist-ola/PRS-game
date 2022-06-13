game_prompt = ["R", "P", "S"]
user_choice = str(input("""
Please select from the options below:
R for rock, 
P for paper, 
S for scissors.
: """)).upper()
for x in game_prompt:
    if user_choice not in game_prompt:
        print("Error! Please input a right game prompt")
        user_choice = str(input("""
        Select from the options below:
        R for rock, 
        P for paper, 
        S for scissors.
        : """)).upper()
        break
import random
CPU_choice = random.choice(game_prompt)
if user_choice == "R":
    selected = "Rock"
elif user_choice == "P":
    selected = "Paper"
elif user_choice == "S":
    selected = "Scissors"

if CPU_choice == "R":
    _selected = "Rock"
elif CPU_choice == "P":
    _selected = "Paper"
elif CPU_choice == "S":
    _selected = "Scissors"
print(f"Player ({selected}) : CPU ({_selected})")

while user_choice == CPU_choice:
    print("It's a tie")
    user_choice = str(input("""
Select a new game prompt:
R for rock,
P for paper,
S for scissors
: """)).upper()
    import random

    CPU_choice = random.choice(game_prompt)
    if user_choice == "R":
        selected = "Rock"
    elif user_choice == "P":
        selected = "Paper"
    elif user_choice == "S":
        selected = "Scissors"

    if CPU_choice == "R":
        _selected = "Rock"
    elif CPU_choice == "P":
        _selected = "Paper"
    elif CPU_choice == "S":
        _selected = "Scissors"
    print(f"Player ({selected}) : CPU ({_selected})")

for x in game_prompt:
    if user_choice == "R" and CPU_choice == "S":
        print("The winner is  Player")
    elif user_choice == "S" and CPU_choice == "R":
        print("The winner is  Computer")
    elif user_choice == "P" and CPU_choice == "R":
        print("The winner is  Player")
    elif user_choice == "R" and CPU_choice == "P":
        print("The winner is  Computer")
    elif user_choice == "S" and CPU_choice == "P":
        print("The winner is  Player")
    elif user_choice == "P" and CPU_choice == "S":
        print("The winner is  Computer")
    break


