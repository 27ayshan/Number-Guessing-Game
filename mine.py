import random

def start_game():
    print("Welcome to the Number Guessing Game ")
    print("I have drawn a number between 1 and 100. Try to find it.")


    secret_regime =random.randint(1,100)
    attempt=0
    while True :
        try:
            guess=int(input("Enter your estimate:"))
            attempt += 1
            

            if guess < secret_regime :
                print("Check for a HIGHER number")
            elif guess > secret_regime :
                print("Check for a LOWER number")
            else:
                print(f"Congratulations! You got it right on {attempt}")
                break
        except ValueError:
            print("Please enter a valid integer!")


start_game()