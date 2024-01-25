#rock paper scissor game with second input randomised
import random
def check (a, b):
    if a == b:
        print("nobody wins!")
    elif a == "rock" and b == "paper":
        print("user 2 wins!")
    elif a== "rock" and b == "scissors":
        print("User 1 wins!")
    elif a== "paper" and b == "rock":
        print("User 1 wins!")
    elif a== "paper" and b == "scissors":
        print("User 2 wins!")
    elif a== "scissors" and b == "rock":
        print("User 2 wins!")
    elif a== "scissors" and b == "paper":
        print("User 1 wins!")
    else:
        print("Invalid input")

print("Welcome to rock, paper and scissors game!")

while True:
    print("valid inputs:\n")
    inputs = ["rock", "paper", "scissors"]
    print(inputs)
    print("\n")
    a = input("User one please enter your choice\n")
    b = random.choice(inputs)
    print("User 2 entered")
    print(b)
    check (a, b)
    choice = input("Keep playing? y/n\n")
    if choice == 'y':
        continue
    else:
        print("Gooodbye!")
        break
