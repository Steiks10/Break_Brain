import random

# Function to generate a random sequence of colors
def generate_colors():
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    secret_code = random.sample(colors, 4)
    return secret_code

# Function to check the guess against the secret code
def check_guess(secret_code, guess):
    correct_color_and_position = 0
    correct_color_only = 0

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_color_and_position += 1
        elif guess[i] in secret_code:
            correct_color_only += 1

    return correct_color_and_position, correct_color_only

# Function to validate the user's guess
def validate_guess(guess):
    valid_colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    if len(guess) != 4:
        return False
    for color in guess:
        if color not in valid_colors:
            return False
    return True

def validate_surrender(surrender):
    if surrender != 'y' and surrender != 'n':
        return False
    return True


# Main game loop
def play_mastermind():
    secret_code = generate_colors()
    attempts = 0

    print("Welcome to Mastermind!")
    print("Guess the code. Valid colors are: \n-->red\n-->blue\n-->green\n-->yellow\n-->orange\n-->purple.")
    print("You will receive feedback after each guess...")
    print("A '+' indicates a correct color in the correct position.")
    print("A '-' indicates a correct color in the wrong position.")
    print("Let's begin!")

    while True:
        guess = input("Enter your guess (e.g., red blue green yellow): ").lower().split()

        if not validate_guess(guess):
            print("Invalid guess. Please enter 4 valid colors.")
            continue

        attempts += 1

        correct_color_and_position, correct_color_only = check_guess(secret_code, guess)

        print("Feedback: " + ("+" * correct_color_and_position) + ("-" * correct_color_only))

        if correct_color_and_position == 4:
            print("CONGRATULATIONS!!! You guessed the secret code in", attempts, "attempts.")
            break
        else:
            if attempts % 5 == 0:
                surrender = input("You give up? (y/n)").lower()
                if validate_surrender(guess):
                    print('Invalid answer')
                    continue
                if surrender == 'y':
                    print("GAME OVER\n The code was", secret_code)
                    break

play_mastermind()