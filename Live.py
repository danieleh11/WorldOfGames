from Utils import screen_cleaner


def welcome(player_name):
    return f"Hello {player_name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"


def load_game():
    chosen_game = ""
    while chosen_game not in ("1", "2", "3"):
        chosen_game = input("Please choose a game to play:\n"
                            "1.Memory Game - a sequence of numbers will appear for 1 second and you have to"
                            " guess it back\n"
                            "2.Guess Game - guess a number and see if you chose like the computer\n"
                            "3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    chosen_difficult = ""
    while chosen_difficult not in ("1", "2", "3", "4", "5"):
        chosen_difficult = input("Please choose game difficulty from 1 to 5:\n")
    return chosen_game, chosen_difficult



