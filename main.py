import random


def main():
    play()


def play():

    # load settings
    options, winner_loser_options = settings()

    # game loop
    while True:

        player = input("Choose Rock, Paper or Scissors:\n").lower()

        if player == "q":
            print("Bye!")
            break

        elif player in options:
            # random option for the computer
            bot = random.choice(options)

            # get the end game results into a list
            end_game = get_end_results(bot)

            # play the game
            print(game(player, bot, winner_loser_options, end_game))

        else:
            # message if player enter wrong choice
            print("choose rock, paper or scissors, or exit the game with \"q\"")


def get_end_results(bot):
    """[get ending result from bot option: draw win or lose]

    Args:
        bot (String): [the bot option]

    Returns:
        [List]: [List of Strings that will display ending of the game]
    """
    game_won = f"Well done. Computer chose {bot} and failed"
    game_lost = f"Sorry, but computer chose {bot}"
    draw = f"There is a draw ({bot})"

    end_game = [game_won, game_lost, draw]

    return end_game


def settings():
    """[game settings]

    Returns:
        [List, Dict]: [the options list and the winning conditions]
    """

    # list of the game options
    options = ['rock', 'paper', 'scissors']

    # dict: winning option (Key) : losing option (Value)
    winner_loser_options = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}
    return options, winner_loser_options,


def game(player, bot, winner_loser_options, end_game):
    """ [play the game]

    Args:
        player (String): the player option (rock, paper, scissors) choice
        bot (String): the computer option (rock, paper, scissors) choice
        winner_loser_options (dict): winning option K to it's losing option V
        end_game (list): strings result to draw [-1], win [0] or lose [1]

    Returns:
        (String): the result of the match
    """

    if player == bot:
        return end_game[-1]
    if bot == winner_loser_options[player]:
        return end_game[0]
    return end_game[1]


main()
