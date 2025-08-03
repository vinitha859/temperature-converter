import random

def guess_number_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("🔻 Too low! Try again.")
            elif guess > secret_number:
                print("🔺 Too high! Try again.")
            else:
                print(f"✅ Correct! The number was {secret_number}.")
                print(f"🎉 You guessed it in {attempts} attempt(s)!")
                break
        except ValueError:
            print("❌ Please enter a valid integer.")

if __name__ == "__main__":
    guess_number_game()
