import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Select difficulty level
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    
    if difficulty == 'easy':
        max_number = 10
        attempts = 5
    elif difficulty == 'medium':
        max_number = 50
        attempts = 7
    else:
        max_number = 100
        attempts = 10

    # Generate a random number
    number_to_guess = random.randint(1, max_number)
    print(f"I've selected a number between 1 and {max_number}. You have {attempts} attempts to guess it.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
    
    else:
        print(f"Sorry, you've used all your attempts! The number was {number_to_guess}.")

number_guessing_game()
