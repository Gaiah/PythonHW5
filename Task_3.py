## 3. Создайте программу для игры в ""Крестики-нолики"".

import random
from tabulate import tabulate
#                                                                 Players names
a = input("Input Your Name, player 1: ")
b = input("Input Your Name, player 2: ")

#                                                                   First move

if  random.randint(1, 2) == 1:                                    
    player_1 = a
    player_2 = b
else:
    player_1 = b
    player_2 = a  


#                                                                Winning combinations
  
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]   

#                                                                 Game table
game = [[1, 2, 3],                                                   
        [4, 5, 6], 
        [7, 8, 9]]

print(tabulate(game, tablefmt="fancy_grid", showindex="never"))


#                                                            Replace the number with a letter


def replace_number(num: int, letter: str):
    global game
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == num:
                game[i][j] = letter
    return game


def add_which_comb(move: int, i_list: list):
    global win
    for i in range(len(win)):
        for j in range(len(win[i])):            
            if win[i][j] == move:
                i_list.append(i)


win_combi = 0
def win_check(i_list: list):
    global win_combi
    for i in range(len(i_list)):
        if i_list.count(i) == 3:
            win_combi = 1
            print(f'win i = {i}')
        


cells = 9
player_1_moves = []
i_list_1 = []
player_2_moves = []
i_list_2 = []


while cells > 0:
    move = int(input(f'{player_1}, make Your move.      '))                               # Player 1 move
    player_1_moves.append(move)
    add_which_comb(move, i_list_1)
    print(f'player 1 moves {player_1_moves}')
    replace_number(move, 'X')
    print(tabulate(game, tablefmt="fancy_grid", showindex="never"))
    win_check(i_list_1)
    if win_combi == 1:
        print(f'You won, {player_1}')
        break

    cells -= 1


    if cells == 0: 
        print("No winner!")
        break

    move = int(input(f'{player_2}, make Your move.      '))                               # Player 1 move
    player_2_moves.append(move)
    add_which_comb(move, i_list_2)
    print(f'player 2 moves {player_2_moves}')
    replace_number(move, 'O')
    print(tabulate(game, tablefmt="fancy_grid", showindex="never"))
    win_check(i_list_2) 
    if win_combi == 1:
        print(f'You won, {player_2}')
        break

    cells -= 1
