# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 19:26:00 2023

@author: 颜名赫
"""

import random

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]


player = {
    'x': 1,
    'y': 1,
    'lives': 10,
    'max_lives': 10,
    'weapon': '',
    'shield': '',
    'potion': 0,
    'character': '战士',
    'damage': 2,
    'max_damage': 2
}

treasure_count = 0
trap_count = 0
monster_count = 0
equipment_count = 0

monsters = [
    {'name': '怪物1', 'health': 4, 'damage': 3},
    {'name': '怪物2', 'health': 4, 'damage': 4},
    {'name': '怪物3', 'health': 4, 'damage': 5}
]

while treasure_count < 3 :
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    if maze[y][x] == '.':
        maze[y][x] = 'T'
        treasure_count += 1

while trap_count < 3:
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    if maze[y][x] == '.':
        maze[y][x] = 'X'
        trap_count += 1

while monster_count < 3:
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    if maze[y][x] == '.':
        monster = random.choice(monsters)
        monster['x'] = x
        monster['y'] = y
        maze[y][x] = 'M'
        monster_count += 1

while equipment_count < 3:
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    if maze[y][x] == '.':
        equipment = random.choice(['W', 'S', 'P'])
        maze[y][x] = equipment
        equipment_count += 1


game_over = False
while not game_over:
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if x == player['x'] and y == player['y']:
                print('\033[91m@\033[0m', end=' ')
            else:
                print(char, end=' ')
        print()

    print(f"位置: ({player['x']}, {player['y']})")
    print(f"生命值: {player['lives']}/{player['max_lives']}")
    print(f"武器: {player['weapon']} (伤害: {player['damage']})")
    print(f"盾牌: {player['shield']}")
    print(f"药品: {player['potion']}")
    print(f"角色性质: {player['character']}")

    action = input("输入w、s、a、d选择行动（上、下、左、右）：")

    if action == "w" and maze[player['y']-1][player['x']] != '#':
        player['y'] -= 1
    elif action == "s" and maze[player['y']+1][player['x']] != '#':
        player['y'] += 1
    elif action == "a" and maze[player['y']][player['x']-1] != '#':
        player['x'] -= 1
    elif action == "d" and maze[player['y']][player['x']+1] != '#':
        player['x'] += 1

    if maze[player['y']][player['x']] == 'T':
        print("恭喜你找到了宝藏！")
        treasure_count -= 1
        maze[player['y']][player['x']] = '.'
        if treasure_count == 0:
            print("你找到了所有的宝藏！游戏胜利！")
            game_over = True
    elif maze[player['y']][player['x']] == 'X':
        print("很可惜，你触碰到了陷阱！")
        trap_count -= 1
        player['lives'] -= 3
        maze[player['y']][player['x']] = '.'
        if trap_count == 0 or player['lives'] == 0:
            print("你已经没有生命了，游戏失败！")
            game_over = True
    elif maze[player['y']][player['x']] == 'M':
        if monster:
            print(f"你遇到了一只{monster['name']}！")
            while player['lives'] > 0 and monster['health'] > 0:
                print(f"怪物生命值: {monster['health']}")
                print(f"你的生命值: {player['lives']}")
                print(f"你对{monster['name']}造成了{player['damage']}点伤害！")
                monster['health'] -= player['damage']
                print(f"怪物生命值：{monster['health']}")
                print(f"我的生命值：{player['lives']}")

                if monster['health'] <= 0:
                    print(f"你成功击败了{monster['name']}！")
                    monster_count -= 1
                    maze[player['y']][player['x']] = '.'
                    if monster_count == 0:
                        print("你战胜了所有的野怪！游戏胜利！")
                        game_over = True
                    break

                player['lives'] -= monster['damage']
                print(f"{monster['name']}对你造成了{monster['damage']}点伤害！")

                if player['lives'] <= 0:
                    print("你已经没有生命了，游戏失败！")
                    game_over = True
        else:
            print("你遇到了一只空怪物！")
        monster_count -= 1
        maze[player['y']][player['x']] = '.'
    elif maze[player['y']][player['x']] == 'W':
        print("你获得了一个剑！")
        maze[player['y']][player['x']] = '.'
        player['weapon'] = '剑'
        player['max_damage'] = 4
        player['damage'] = player['max_damage']
        equipment_count -= 1
    elif maze[player['y']][player['x']] == 'S':
        print("你获得了一个盾牌！")
        maze[player['y']][player['x']] = '.'
        player['shield'] = '盾牌'
        player['max_lives'] = 15
        player['lives'] = 15
        equipment_count -= 1
    elif maze[player['y']][player['x']] == 'P':
        print("你获得了一个药品！")
        maze[player['y']][player['x']] = '.'
        player['potion'] += 1
        if player['lives'] < player['max_lives']:
            player['lives'] += 3
            print("使用了一瓶药水！生命值恢复了！")
            player["potion"] -=1
        equipment_count -= 1