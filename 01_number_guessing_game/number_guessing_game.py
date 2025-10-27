import random
import time

attempts = 1
guesses = []

def line():
    print("-" * 36)

levels = {
    1: {'Level': 'Easy', 'Chances': 10},
    2: {'Level': 'Medium', 'Chances': 5},
    3: {'Level': 'Hard', 'Chances': 3}
}

# When the game starts, it should display a welcome message along with the rules of the game.
line()
print("Welcome to the Number Guessing Game!")
line()
print("Please select the difficulty level:")

for key, info in levels.items():
    print(f"{key}. {info['Level']} (Chances: {info['Chances']})")

line()

# The computer should randomly select a number between 1 and 100.
computer_random = random.randint(1, 100)

# User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
choice = int(input("Enter your choice of level: "))

level = levels[choice]['Level']
chances = levels[choice]['Chances']

print(f"\nGreat! You have selected the {level} difficulty level.\nYou have {chances} chances to guess the correct number.")
time.sleep(1)
print("\nI'm thinking of a number between 1 and 100.")
time.sleep(2)
print("\nLet's start the game!")
time.sleep(1)


while True:
# The game should end when the user guesses the correct number or runs out of chances.
    if attempts > chances:
        print(f"\nYou’ve run out of chances! ({attempts - 1}/{chances})")
        print(f"You guesses: {', '.join(map(str, guesses))}")
        print(f"\nThe correct answer is: {computer_random}")
        break

# The user should be able to enter their guess.
    guess = int(input("\nEnter your guess: "))

# If the user's guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
    if guess == computer_random:
        print(f"\nCongratulations! You guessed the correct number '{computer_random}' in {attempts} attempts.")
        print()
        break

# If the user's guess is incorrect, the game should display a message indicating whether the number is greater or less than the user's guess.
    else:
        print(f"Incorrect! The number is {'less' if guess > computer_random else 'greater'} than {guess}.")
        guesses.append(guess)
        attempts += 1