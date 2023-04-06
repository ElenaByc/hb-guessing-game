"""A number-guessing game."""


import random
name = input("Howdy, what's your name?\n(type in your name): ")
range_min = int(input("Howdy, please add minimum range number: "))
range_max = int(input("Howdy, please add maximum range number: "))
limit_num = int(input("Please set the max number of guesses? "))
role = int(input("Please choose the role: 1. player, 2. presenter "))
best_score = float('inf')
tries = 0


def guess_game(min, max):
    tries = 0
    guess = None
    secret_num = random.randint(min, max)
    while guess != secret_num and tries < limit_num:
        guess = int(input('Your guess? '))
        tries += 1
        if guess < secret_num:
            print('Your guess is too low, try again.')
        elif guess > secret_num:
            print('Your guess is too high, try again.')
        else:
            global best_score
            if tries < best_score:
                best_score = tries
            print(
                f'Well done, {name}! You found my number in {tries} tries! and your best score is {best_score}')
            break
        if tries == limit_num:
            print('Too many times!!')
            break

def guess_game_computer(min, max):
    tries = 1
    mid = (min + max) // 2
    respond = input(f"The computer guess is {mid} (l for low, h for high, c for correct)").lower()
    while respond != 'c':
        if respond =='l':
            min = mid + 1
        else:
            max = mid - 1
        mid = (min + max) // 2
        tries += 1
        respond = input(f"The computer guess is {mid} (l for low, h for high, c for correct)").lower()
    print(f"The computer won with {tries} attempts!")

    
if role == 1:
    print(f"{name}, I'm thinking of a number between {range_min} and {range_max}: ")
    guess_game(range_min, range_max)

    play_again = input('Do you want to play again?(Y/N) ').lower()
    while play_again != 'n':
        guess_game(range_min, range_max)
        play_again = input('Do you want to play again?(Y/N) ').lower()
else:
    num = int(input(f"{name}, Please choose a number between {range_min} and {range_max}: "))
    print(f"Your secret number is {num}")
    guess_game_computer(range_min, range_max)