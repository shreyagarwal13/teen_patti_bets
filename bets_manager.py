class colors:
    """Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold"""

    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        lightgrey = "\033[47m"


# This script is used to track the bets in each round of a teen patti game
import json
import os.path
from prettytable import PrettyTable

players = {}
print(
    colors.fg.lightred
    + "Don't Fiddle with the game else the game will fiddle with you!! "
    + colors.reset
)
winning_history_path = "winning_history.json"
check_file = os.path.isfile(winning_history_path)
load_game = "n"
if check_file:
    load_game = input("We found saved balances, do you want to load them? (y/n) ")


def check_return_int_conversion(string):
    if string == "-1":
        return -1
    if string.isnumeric():
        return int(string)
    else:
        print(
            colors.bold + colors.fg.red + "Invalid Input!!, Ending Game" + colors.reset
        )
        exit(0)


def check_yes_no(yes_no_ip):
    if yes_no_ip.lower() == "y":
        return True
    else:
        return False


def save_data():
    with open(winning_history_path, "w", encoding="utf-8") as json_file:
        json.dump(players, json_file)
        print(colors.fg.green + "\nPlayer Data saved!\n" + colors.reset)


def input_players():
    num = 0
    while num < 2:
        num = check_return_int_conversion(
            input(
                colors.fg.lightcyan + "Enter number of players: " + colors.fg.lightgreen
            )
        )
        if num < 2:
            print(
                colors.fg.lightred
                + "No no, do it again, this time atleast 2 players."
                + colors.reset
            )
    for i in range(num):
        player_name = input(
            colors.fg.lightcyan
            + "\nEnter name of Player number "
            + str(i + 1)
            + " "
            + colors.fg.lightgreen
        )
        player_balance = check_return_int_conversion(
            input(
                colors.fg.lightcyan
                + "Enter balance of "
                + player_name.title()
                + " "
                + colors.fg.lightgreen
            )
        )
        players[i + 1] = {"id": i + 1, "balance": player_balance, "name": player_name}
    print_player_balances()


def get_new_player_number():
    return list(players)[-1] + 1


def add_remove_player():
    add_remove_player_check = check_return_int_conversion(
        input(
            colors.fg.lightred
            + "\nDo you want to add(1)/remove(2) player?\nEnter any other number to not take any action: "
            + colors.fg.lightgreen
        )
    )
    while add_remove_player_check == 1:
        player_number = get_new_player_number()
        player_name = input(
            colors.fg.lightcyan
            + "\nEnter name of Player number "
            + str(player_number)
            + " "
            + colors.fg.lightgreen
        )
        player_balance = check_return_int_conversion(
            input(
                colors.fg.lightcyan
                + "Enter balance of "
                + player_name.title()
                + " "
                + colors.fg.lightgreen
            )
        )
        players[player_number] = {
            "id": player_number,
            "balance": player_balance,
            "name": player_name,
        }
        add_remove_player_check = check_return_int_conversion(
            input(
                colors.fg.lightred
                + "\nDo you want to add another player? \nEnter 1 for yes, 2 for player deletion, any other number for quitting "
                + colors.fg.lightgreen
            )
        )

    while add_remove_player_check == 2:
        if len(list(players)) == 0:
            print(
                colors.bold
                + colors.fg.lightred
                + "Noooo I won't let you do this. Haha!"
                + colors.reset
            )
        print_players()
        player_number = check_return_int_conversion(
            input(
                colors.fg.lightcyan
                + "Enter the player number you want to remove: "
                + colors.fg.lightgreen
            )
        )
        if not players.get(player_number):
            print(
                colors.bold
                + colors.fg.red
                + "Do you think I am Dumb?? I am not but you definitely are!!"
                + colors.reset
            )
        else:
            players.pop(player_number)
        add_remove_player_check = check_return_int_conversion(
            input(
                colors.fg.lightcyan
                + "\nDo you want to remove another player (Enter 2 for yes, any other number for quitting) "
                + colors.fg.lightgreen
            )
        )
    save_data()


def print_player_balances():
    table = PrettyTable(["No.", "Name", "Balance"], title="Player Balances")
    for k, v in players.items():
        table.add_row([k, v.get("name").title(), "Rs. " + str(v.get("balance"))])
    print(table)


def print_players():
    table = PrettyTable(["No.", "Name"], title="Players")
    for k, v in players.items():
        table.add_row([k, v.get("name").title()])
    print(table)


def generate_round():
    print(colors.fg.lightcyan + "\nStarting new round! ")
    starting_player_id = check_return_int_conversion(
        input("Enter the player number who starts this round " + colors.fg.lightgreen)
    )
    if not players.get(starting_player_id):
        print(
            colors.bold
            + colors.fg.red
            + "Do you think I am Dumb!! , Now go ahead do everything again!"
            + colors.reset
        )
        exit(0)
    print(
        colors.fg.lightcyan
        + "\nThe bets will start from "
        + players.get(starting_player_id).get("name").title()
    )
    num_of_players = len(players)
    print(colors.fg.blue + "\nEnter bets of players")
    print("  0 : Fold")
    print(" -1 : End Betting\n" + colors.fg.lightcyan)
    player_bet = 0
    winning_amount = 0
    winning_player_id = None
    folded_players = {}
    player_id = starting_player_id
    round_history = {k: 0 for k in players.keys()}
    while player_bet != -1:
        print(colors.fg.lightcyan + "", end="")
        player_name = players.get(player_id).get("name").title()
        if folded_players.get(player_id):
            player_id = player_id % num_of_players + 1
            continue
        player_bet = check_return_int_conversion(
            input(player_name + " Bets Rs. " + colors.fg.lightgreen)
        )
        if player_bet == -1:
            break
        elif player_bet == 0:
            print(colors.fg.lightcyan + "\n" + player_name + " Folds \n")
            folded_players[player_id] = True
        players[player_id]["balance"] -= player_bet
        round_history[player_id] -= player_bet
        winning_amount += player_bet
        player_id = player_id % num_of_players + 1
        if len(list(folded_players)) == len(list(players)) - 1:
            winning_player_id = player_id
            break

    if not winning_player_id:
        print_players()
        winning_player_id = check_return_int_conversion(
            input(
                colors.fg.lightcyan
                + "Enter the player number who won this round "
                + colors.fg.lightgreen
            )
        )

    if not players.get(winning_player_id):
        print(
            colors.bold
            + colors.fg.red
            + "Do you think I am Dumb!! , Now go ahead do everything again!"
            + colors.reset
        )
        exit(0)

    winning_player_name = players.get(winning_player_id).get("name")
    print(
        colors.fg.lightgreen
        + "\nCongratulations! "
        + winning_player_name.title()
        + " won the pot of Rs. "
        + str(winning_amount)
    )
    players[winning_player_id]["balance"] += winning_amount
    round_history[winning_player_id] += winning_amount
    print_player_balances()
    save_data()
    add_remove_player()


if check_yes_no(load_game):
    print(colors.fg.lightgreen + "Loading saved game ....")
    with open(winning_history_path, "r", encoding="utf-8") as json_file:
        try:
            players = json.load(json_file)
            players = {int(k): v for k, v in players.items()}
            print_player_balances()
            add_remove_player()
        except:
            print(
                colors.fg.lightred + "\n Sorry, no data found. Starting new game... \n"
            )
            input_players()
else:
    input_players()


game_status = "y"
while check_yes_no(game_status):
    generate_round()
    game_status = input(
        colors.fg.lightgreen + "Do you want to start to next round ? (y/n) "
    )
