import random


def game():
    game_over_flag = False
    while not game_over_flag:
        print('!')


if input('Начать игру? (да/нет):').lower == 'да':
    game()
