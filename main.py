from random import randint
from math import floor

# if __name__ == '__main__':


did_guess: bool = False

attempts:int = 0

def calculate_score(tries: int):
    return floor( (10 / tries) + tries * 100 )



while not did_guess:
    try:

        current_level: int = 10
        print(f"1 to {current_level}")

        RANDOM = randint(1, current_level)
        user_input = int(input("Guess >> "))
        print(f"u said :{user_input} and AI said: {RANDOM}")

        attempts += 1

        if RANDOM == user_input:

            print(f"You won! With {attempts} tries, and you guessed: {user_input} and AI chose: {RANDOM}")
            print(f"Score is: { calculate_score(attempts) }")
            did_guess = True

    except (ValueError):
        print("please enter a number")