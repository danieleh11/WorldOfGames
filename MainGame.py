from CurrencyRouletteGame import play_currency
from Live import welcome, load_game
from GuessGame import play_guess
from MainScores import app
from MemoryGame import play_memory
from Score import add_score, zero_on_score

# Ask player for name
from Utils import screen_cleaner


zero_on_score()

player_name = input("Enter you name: ")
print(welcome(player_name))


def choose_game(chosen_game, chosen_difficult):
    if chosen_game == 1:
        m = play_memory(chosen_difficult)
        if m:  # if m is true call the func to add points
            add_score(chosen_difficult)
    elif chosen_game == 2:
        g = play_guess(chosen_difficult)
        if g:  # if g is true call the func to add points
            add_score(chosen_difficult)
    else:
        c = play_currency(chosen_difficult)
        if c:  # if c is true call the func to add points
            add_score(chosen_difficult)


def play_again():
    play_more = input('Play again  - Y or N ?')
    if play_more == 'y' or play_more == 'Y':
        chosen_game, chosen_difficult = load_game()
        choose_game(int(chosen_game), int(chosen_difficult))
    else:
        print('Thanks for playing, Goodbye')


chosen_game, chosen_difficult = load_game()

choose_game(int(chosen_game), int(chosen_difficult))
screen_cleaner()
play_again()
if __name__ == '__main__':
    app.run(host='localhost', debug=False, threaded=False, port=8777)

