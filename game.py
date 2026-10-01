import random

computer_score = 0
my_score = 0

choices = ["rock", "paper", "scissors"]

print("Welcome to RPS!!!")

while True:
#     my_choice = input("put in your choice in this list + str(choices)")
#     computer_choice = random.choice(choices)

#     if  my_choice == "rock" and computer_choice == "paper":
#         print("computer wins, you lost!")
#         computer_score += 1
#     elif my_choices ==

    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    random_number = random.randint(0, 2)
    computer_pick = choices[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        my_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        my_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        my_score += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_score += 1

print(f"Your score: {my_score}")
print(f"Computer's score: {computer_score}")