import random

def numberGame():
    number : int = random.randint(1,101)

    print("Guess the number in 1-100 range")

    while True:
        numberGuess : int = int(input(">>> "))
        if numberGuess > number:
            print("Try lower")
        elif numberGuess < number:
            print("Try higher")
        else:
            print("You won!")
            break

name : str = input("Enter your name: ")

while True:
    choice : str = input(f"Hello {name} would you like to play guess the number game? (y/n): ")

    if choice.lower() == "y":
        numberGame()
        break
    elif choice.lower() == "n":
        break
    else:
        print("Invalid input")

print("Bye")
