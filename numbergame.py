from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose your difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

def check_answer(answer, number, turns):
    if answer > number:
        print("Too High")
        return turns - 1
    if answer < number:
        print("Too Low")
        return turns - 1
    if answer == number:
        print(f"You got it! The answer was {answer}")
        return turns

def game():

    print("Welcome to the Number Guessing Games!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != chosen_number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, chosen_number, turns)

        if turns == 0:
            print("You've run out of guesses. You lose")
            return print(f"The correct answer was {chosen_number}.")
        elif guess!= chosen_number:
            print("Guess again.")


print(logo)
game()