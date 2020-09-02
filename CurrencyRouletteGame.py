import random

from forex_python.converter import CurrencyRates


def get_money_interval(chosen_difficult):
    rate = CurrencyRates()
    t = random.randint(1, 101)
    print(f"the number in dollars is {t}")
    total_amount = rate.get_rate('USD', 'ILS')* t
    low = total_amount - (5 - chosen_difficult)
    high = total_amount + (5 - chosen_difficult)
    return low, high


def get_guess_from_user():
    user_guess = input(f"enter a guess of value to a given amount of ILS :")
    user_guess = float(user_guess)
    return user_guess


def play_currency(chosen_difficult):
    low, high = get_money_interval(chosen_difficult)
    get_user_guess = get_guess_from_user()

    if low < get_user_guess < high:
        print("User Won!")
        print(f" the range was between {low} and {high}. your guess = {get_user_guess}")
    else:
        print("User Lost!")
        print(f" the range was between {low} and {high}. your guess = {get_user_guess}")
