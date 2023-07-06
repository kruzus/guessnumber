from random import randint
from math import floor

import os

def clear_screen():
    # Clear screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen for Unix/Linux/MacOS
    else:
        os.system('clear')



#
# did_guess: bool = False
#
# attempts: int = 0
#
#
# def calculate_score(tries: int) -> int:
#     return floor((2 / tries) * 5000 / 2)
#
#
# while not did_guess:
#     try:
#         current_level: int = 10
#         print(f"1 to {current_level}")
#
#         RANDOM = randint(1, current_level)
#         user_input = int(input("Guess >> "))
#         print(f"u said :{user_input} and AI said: {RANDOM}")
#
#         attempts += 1
#
#         if RANDOM == user_input:
#             FINAL_SCORE = calculate_score(attempts)
#
#             if FINAL_SCORE >= 30:
#                 print(f"Nice I guess... you won, with {attempts} tries.... wow... ")
#                 print(f"Your final score: {FINAL_SCORE}")
#             elif FINAL_SCORE <= 25:
#                 print("Not that great but nice i guess... you won.")
#                 print(f"Your final score: {FINAL_SCORE}")
#             elif FINAL_SCORE <= 15:
#                 print(f"You won! With {attempts} tries, and you guessed: {user_input} and AI chose: {RANDOM}")
#                 print(f"Score is: {calculate_score(attempts)}")
#
#             did_guess = True
#
#     except (ValueError):
#         print("please enter a number")


class GuessGame:
    _did_guess: bool = False
    _attemtps: int = 0
    _playerName: str = ""
    _endless: bool = False
    _current_level: int = 10
    

    def __init__(self, name: str, endless: bool = False):
        self._playerName = name
        self._endless = endless

    def play(self):
        print(f"Welcome {self._playerName} guess number from 1-10!")
        print("Mode: Easy!")
        while not self._did_guess:
            try:


                print(f"1 to {self._current_level}")

                RANDOM = randint(1, self._current_level)
                user_input = int(input("Guess >> "))
                print(f"u said :{user_input} and AI said: {RANDOM}")

                self._attemtps += 1

                if RANDOM == user_input:
                    self._current_level *= 2

                    FINAL_SCORE = floor((2 / self._attemtps) * 5000 / 2)

                    print(f"{self._playerName} you won with the score of {FINAL_SCORE}!")
                    print(f"{self._attemtps} attempts.")

                    if self._endless:
                        self._did_guess = False
                    else:
                        self._did_guess = True

            except (ValueError):
                print("please enter a number")


game = GuessGame("Bek")

if __name__ == '__main__':
    game.play()
