import random


def generate_number(chosen_difficult):
    secret_number = random.randint(1, chosen_difficult)
    return secret_number


def get_guess_from_user(chosen_difficult):
    user_guess = input(f"enter number between 1 to {chosen_difficult} :")
    return int(user_guess)


def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        print(f"User Won! user input={user_guess} , comp input={secret_number}")
        return True
    else:
        print(f"User Lost! user input={user_guess} , comp input={secret_number}")
        return False


def play_guess(chosen_difficult):
    secret_number = generate_number(chosen_difficult)
    user_guess = get_guess_from_user(chosen_difficult)
    return compare_results(secret_number, user_guess)


