# -*- coding: utf-8 -*-
# 井字棋游戏
from os import system

def print_board(board):
    print(board['WN']+'|'+board['NN']+'|'+board['EN'])
    print('-+-+-')
    print(board['WW']+'|'+board['CC']+'|'+board['EE'])
    print('-+-+-')
    print(board['WS']+'|'+board['SS']+'|'+board['ES'])


def is_player_win(board, player):
    pieces = list(board.values())  # 将棋盘字典的值存为列表
    pla_had = []  # 存储玩家占下的格子数
    win_had = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # 获胜条件
    if pieces.count(player) >= 3:
        # 如果玩家至少下了三个棋子通过
        for i in range(9):
            # 遍历九个格子，将已占格子的编号加入列表
            if pieces[i] == player:
                pla_had.append(i+1)
        for lis in win_had:
            # 遍历胜利条件，如果已占格子列表包含某个胜利列表，返回True
            if set(lis) <= set(pla_had):
                return True
    else:
        return False


def main():
    print('新的一局井字棋开始了，九格占满后游戏结束')
    init_board = {
        'WN': 'WN', 'NN': 'NN', 'EN': 'EN',
        'WW': 'WW', 'CC': 'CC', 'EE': 'EE',
        'WS': 'WS', 'SS': 'SS', 'ES': 'ES'
    }
    begin = True
    while begin:
        begin = False
        curre_board = init_board.copy()
        counter = 0
        player = 'X'
        print_board(curre_board)
        while counter < 9:
            move = input('轮到玩家%s走棋，请输入位置编号：' % player)
            while move not in curre_board.keys() or curre_board[move] != move:
                move = input('选择的位置已有棋或输入格式不对，请重新输入：')
            curre_board[move] = player
            counter += 1
            print_board(curre_board)
            if is_player_win(curre_board, player):
                print('恭喜玩家%s胜利！游戏结束。' % player)
                break
            if player is 'X':
                player = 'O'
            else:
                player = 'X'

        choice = input('还要继续进行下一局吗？Y/N:')
        begin = choice == 'Y'


main()


