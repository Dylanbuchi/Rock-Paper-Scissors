import random


def main():

    # list of the game options
    options = ['rock', 'paper', 'scissors']

    # random option for the computer
    bot = random.choice(options)

    # dict: winning option (Key) : losing option (Value)
    winner_loser_options = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}

    # strings for the game endings, then put it in a list
    game_won = f"Well done. Computer chose {bot} and failed"
    game_lost = f"Sorry, but computer chose {bot}"
    draw = f"There is a draw ({bot})"

    end_game = [game_won, game_lost, draw]

    # get player choice
    player = input("Choose Rock, Paper or Scissors\n").lower()

    # play
    print(play(player, bot, winner_loser_options, end_game))


def play(player, bot, winner_loser_options, end_game):
    """ method to play the game

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
