#This script is used to track the bets in each round of a teen patti game
import json 
import os.path

players = {}

winning_history_path = 'winning_history.json'
check_file = os.path.isfile(winning_history_path)
load_game = "n"
if check_file:
    load_game = input("We found saved balances, do you want to load them? (y/n) ")

def check_yes_no(yes_no_ip):
    if yes_no_ip.lower() == "y":
        return True
    else:
        return False

def save_winnings():
    with open(winning_history_path, 'w', encoding='utf-8') as json_file:
        json.dump(players, json_file)
        print('\nPlayer balances saved!\n')

def input_players():
    num = int(input("Enter number of players "))
    for i in range(num):
        player_name = input("\nEnter name of Player number "+str(i+1)+" ")
        player_balance = int(input("Enter balance of "+player_name+" "))
        players[i+1] = {
            "id":i+1,
            "balance":player_balance,
            "name":player_name
        }
    print_player_balances()

def get_new_player_number():
    new_player_number = 1
    for k, v in players.items():
        if v.get("id")>=new_player_number:
            new_player_number = v.get("id")+1
    return new_player_number

def add_new_player():
    add_new_player_check = input("\nDo you want to add new player? (y/n)  ")
    while check_yes_no(add_new_player_check):
        player_number = get_new_player_number()
        player_name = input("\nEnter name of Player number "+str(player_number)+" ")
        player_balance = int(input("Enter balance of "+player_name+" "))
        players[player_number] = {
            "id":player_number,
            "balance":player_balance,
            "name":player_name,
        }
        add_new_player_check = input("\nDo you want to add another player? (y/n)  ")

def print_player_balances():
    print("\nBalances of each player are")
    print("\n No. \t Name \t Balance")
    for k, v in players.items():
        print(" "+str(k)+"\t"+v.get("name")+"\t: Rs. "+str(v.get("balance")))

def generate_round():
    print("\nStarting new round! ")
    starting_player_id = int(input("Enter the player number who starts this round "))
    print(players)
    print("\nThe bets will start from "+players.get(starting_player_id).get("name"))
    num_of_players = len(players)
    print("\nEnter bets of players")
    print("  0 : Fold")
    print(" -1 : End Betting\n")
    player_bet = 0
    winning_amount = 0
    folded_players = {}
    player_id = starting_player_id
    round_history = { k: 0 for k in players.keys()}
    while(player_bet!=-1):
        player_name = players.get(player_id).get("name")
        if folded_players.get(player_id):
            player_id = player_id%num_of_players + 1
            continue
        player_bet = int(input(player_name+" Rs. "))
        if player_bet==-1:
            break
        elif player_bet == 0:
            print("\n"+player_name+" Folds ⨯\n")
            folded_players[player_id] = True
        players[player_id]["balance"]-=player_bet
        round_history[player_id] -= player_bet
        winning_amount+=player_bet
        player_id = player_id%num_of_players + 1
    winning_player_id = int(input("Enter the player number who won this round "))
    winning_player_name = players.get(winning_player_id).get("name")
    print("\n Congratulations! "+winning_player_name+" won the pot of Rs. "+str(winning_amount))
    players[winning_player_id]["balance"] += winning_amount
    round_history[winning_player_id] += winning_amount
    print_player_balances()
    save_winnings()
    add_new_player()
    
if check_yes_no(load_game):
    print("Loading saved game ....")    
    with open(winning_history_path, 'r', encoding='utf-8') as json_file:
        try:
            players = json.load(json_file)
            players = {int(k):v for k,v in players.items()}
            print_player_balances()
            add_new_player()
        except:
            print("\n Sorry, no data found. Starting new game... \n")
            input_players()

else:
    input_players()


game_status = "y"
while(check_yes_no(game_status)):
    generate_round()
    game_status = input("Do you want to start to next round ? (y/n) ")






