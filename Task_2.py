# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random

print("Choose one of the game modes: 1 - Player vs Player. 2 - Player vs bot. 3 - Player vs AI.")
mode = int(input())

if mode == 1:                                                                     # Players names
    a = input("Input Your Name: ")
    b = input("Input Your Name: ")
elif mode == 2:
    a = input("Input Your Name: ")
    b = "Bot"
elif mode == 3:
    a = input("Input Your Name: ")
    b = "AI"
    

if  random.randint(1, 2) == 1:                                                    # Жеребьёвка
    player_1 = a
    player_2 = b
else:
    player_1 = b
    player_2 = a  

candies = 2021

def player_move(player):                                                                # players' moves
    if player == "Bot":
        player_num = random.randint(1, 28)
        return player_num
    elif player == "AI":
        if candies < 29:
            player_num = candies
        elif candies < 57:
            player_num = candies - 29
        else:
            player_num = random.randint(1, 28)                                                                   
        return player_num
    else:
        playernum = int(input(f"{player}, Input a number 1 - 28: "))
        if 1 > playernum > 28:
            print(f"Incorrect number. You are out, {player}!")
        else:
            return playernum
  



if mode == 1:
    while candies > 0:                                                                                              # Game mode 1
        candies -= player_move(player_1)
        print(f"{candies} candies left on the table")
        if candies < 1:
            print(f"And You won, {player_1}!")
            break
        candies -= player_move(player_2)
        print(f"{candies} candies left on the table")
        if candies < 1:
            print(f"You won, {player_2}!")
elif mode == 2:
    while candies > 0:
        player_1_int = player_move(player_1)                                                                         # Game mode 2
        candies -= player_1_int
        print(f"{player_1}'s move is: {player_1_int}. {candies} candies left on the table")
        if candies < 1:
            print(f"And You won, {player_1}!")
            break
        player_2_int = player_move(player_2)
        candies -= player_2_int
        print(f"{player_2}'s move is: {player_2_int}. {candies} candies left on the table")
        if candies < 1:
            print(f"And You won, {player_2}!")
elif mode == 3:                                                                                                      # Game mode 3 
    while candies > 0:
        player_1_int = player_move(player_1)
        candies -= player_1_int
        print(f"{player_1}'s move is: {player_1_int}. {candies} candies left on the table")
        if candies < 1:
            print(f"And You won, {player_1}!")
            break
        player_2_int = player_move(player_2)
        candies -= player_2_int
        print(f"{player_2}'s move is: {player_2_int}. {candies} candies left on the table")
        if candies < 1:
            print(f"You won, {player_2}!")
else:
    print("Try one more time")