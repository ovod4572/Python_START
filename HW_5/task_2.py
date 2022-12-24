"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""
import time
import random

def player_move(min_pick_up: int, max_pick_up: int) -> int:
    candy_out = -1
    while candy_out < min_pick_up or candy_out > max_pick_up:
        candy_out = int(input(f'Сколько конфет Вы забираете? '
            f'Введите количество от {min_pick_up} до {max_pick_up}: '))
        if candy_out < min_pick_up or candy_out > max_pick_up:
            print(f'Вы хотите забрать {candy_out} конфет? А по правилам можно взять '
                f'не меньше {min_pick_up} и не больше {max_pick_up}, увы.')
    return candy_out

def bot_random(min_pick_up: int, max_pick_up: int) -> int:
    return random.randint(min_pick_up, max_pick_up)

def win_algorithm(candy_on_table: int, min_pick_up: int, max_pick_up: int) -> int:
    way_num = candy_on_table - max_pick_up - min_pick_up
    if way_num >= min_pick_up and way_num < min_pick_up + max_pick_up:
        return way_num
    else:
        way_num = max_pick_up 
        return way_num

def spelling(number_candies: int) -> str:
    spell = 'конфет'
    ones = [1, 21]
    twines = [2, 3, 4, 22, 23, 24]
    if number_candies in ones:
        spell = 'конфету'
    elif number_candies in twines:
        spell = 'конфеты' 
    return spell


player_1 = input('Вы - первый игрок, представьтесь, пожалуйста: ')
if input('Вы будете играть против другого игрока, введите "Y": ') == 'Y':
    player_2 = input('Представьте, пожалуйста, своего противника: ')
else:
    player_2 = 'Bot'
    bot_level = input('Вы хотите играть с продвинутым ботом, введите "Y".\n'
    'Если с "дурачком" - любой другой символ: ')
    if bot_level == 'Y':
        bot_level = 1
    else:
        bot_level = 2
    
candy_on_table = int(input('Сколько конфет будем разыгрывать? '))
min_pick_up = int(input('Сколько минимально будем брать конфет за один ход? '))
max_pick_up = int(input('Сколько максимально будем брать конфет за один ход? '))
player_dict = {1: player_1, 2: player_2}
print('Проводим жеребьёвку первого хода.')
player_num = int(time.time()//1%2+1)
print(f'Первым ходит {player_dict[player_num]}')
print('НАЧАЛИ!!!')
candy_out = 0
while candy_on_table > 0:
    if player_dict[player_num] != 'Bot':
        candy_out = player_move(min_pick_up, max_pick_up)
    elif bot_level == 1:
        candy_out = win_algorithm(candy_on_table, min_pick_up, max_pick_up)
    else:
        candy_out = bot_random(min_pick_up, max_pick_up)
    candy_on_table = candy_on_table - candy_out
    print(f'{player_dict[player_num]} забрал {candy_out} {spelling(candy_out)}.\n'
        f'На столе осталось {candy_on_table} {spelling(candy_on_table)}.')
    if player_num + 1 > 2:
        player_num = 1
    else:
        player_num = 2
if player_num + 1 > 2:
    player_num = 1
else:
    player_num = 2  
print('!!!') 
print(f'ИГРА ЗАВЕРШИЛАСЬ ПОБЕДОЙ ИГРОКА {player_dict[player_num]}!!!')
print()
