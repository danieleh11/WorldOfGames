from CurrencyRouletteGame import play_currency
from Live import welcome, load_game
from GuessGame import play_guess
from MemoryGame import play_memory

# Ask player for name
player_name = input("Enter you name: ")
print(welcome(player_name))


def choose_game(chosen_game, chosen_difficult):
    if chosen_game == 1:
        play_memory(chosen_difficult)
    elif chosen_game == 2:
        play_guess(chosen_difficult)
    else:
        play_currency(chosen_difficult)


chosen_game, chosen_difficult = load_game()

choose_game(int(chosen_game), int(chosen_difficult))
