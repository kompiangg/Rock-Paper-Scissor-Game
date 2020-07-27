import random


def player(name, weapon):
    weapon_list = ['Scissor', 'Paper', 'Stone']
    print(name, ' picked ', weapon_list[weapon])
    print('Computer picked ', weapon_list[weapon_comp])


def validate():
    if 0 > weapon_player or weapon_player > 2:
        return False
    return True


def versus():
    if weapon_comp == weapon_player:
        return 'Draw'
    elif weapon_comp == 0 and weapon_player == 1:
        return 'Lose'
    elif weapon_comp == 1 and weapon_player == 2:
        return 'Lose'
    elif weapon_comp == 0 and weapon_player == 2:
        return 'Lose'
    return 'Win'


print('Starting the game!')
name_player = input('Input your name: ')
weapon_player = int(input('Pick your weapon (0[Stone], 1[Scissor] , 2[Paper]): '))
weapon_comp = random.randint(0, 2)

if validate():
    player(name_player, weapon_player)
    print(versus())

else:
    print('Input valid number')
