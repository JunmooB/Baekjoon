import sys
input = sys.stdin.readline

def check_bomb(index, value, num):
    if index == 0:
        if value == 1:
            if bomb_list[0:2].count('*') == 1:
                if bomb_list[index] == '*':
                    bomb_list[index + 1] = '0'
                else:
                    bomb_list[index] = '0'
        elif value == 0:
            bomb_list[index] = bomb_list[index+1] = '0'
        else:
            bomb_list[index] = bomb_list[index+1] = '*'

    elif index == num -1:
        if value == 1:
            if bomb_list[num-2:num].count('*') == 1:
                if bomb_list[index] == '*':
                    bomb_list[index - 1] = '0'
                else:
                    bomb_list[index] = '0'
        elif value == 0:
            bomb_list[index] = bomb_list[index-1] = '0'
        else:
            bomb_list[index] = bomb_list[index-1] = '*'

    else: # index가 0과 끝이 아닌 경우
        if value == 0:
            for ind in range(index-1, index+2):
                bomb_list[ind] = '0'
        elif value == 1:
            if bomb_list[index-1:index+2].count('*') == 1:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] != '*':
                        bomb_list[ind] = '0'
            elif bomb_list[index-1:index+2].count('0') == 2:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] != '0':
                        bomb_list[ind] = '*'

        elif value == 2:  # 이 경우에 '0'이 섞여 있는 경우 문제
            if bomb_list[index-1:index+2].count('*') == 2:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] != '*':
                        bomb_list[ind] = '0'
            elif bomb_list[index-1:index+2].count('*') == 1 and bomb_list[index-1:index+2].count('0') == 1:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '*'
            elif bomb_list[index-1:index+2].count('*') == 0 and bomb_list[index-1:index+2].count('0') == 1:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '*'
        else: # value가 3인 경우
            for ind in range(index-1, index+2):
                bomb_list[ind] = '*'

def max_bomb(index, value, num):
    if index == 0:
        if value == 1:
            if bomb_list[index:index+2].count('*') == 0:
                temp = 0
                for ind in range(index, index+2):
                    if bomb_list[ind] == '#' and temp < 1:
                        bomb_list[ind] = '*'
                        temp += 1
                    elif bomb_list[ind] == '#' and temp == 1:
                        bomb_list[ind] = '0'
    
    elif index == num -1:
        if bomb_list[index-1:index+1].count('*') == 0:
            temp = 0
            for ind in range(index-1, index+1):
                if bomb_list[ind] == '#' and temp < 1:
                    bomb_list[ind] = '*'
                    temp += 1
                elif bomb_list[ind] == '#' and temp == 1:
                    bomb_list[ind] = '0'
    else:
        # value가 3인 경우 (x)
        # value가 1인 경우 ('0')  ### ##0
        if value == 1:
            if bomb_list[index-1:index+2].count('*') == 1:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '0'
            else:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '*'
                        break                

        else :# value가 2인 경우 ('0'이 하나도 없을 때)
            if bomb_list[index-1:index+2].count('*') == 2:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '0'
            elif bomb_list[index-1:index+2].count('*') == 1:
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#':
                        bomb_list[ind] = '*'
                        break
            else:
                temp = 0
                for ind in range(index-1, index+2):
                    if bomb_list[ind] == '#' and temp < 2:
                        bomb_list[ind] = '*'
                        temp += 1
                    elif bomb_list[ind] == '#' and temp == 2:
                        bomb_list[ind] = '0'          
        




t = int(input())
for _ in range(t):
    n = int(input())
    num_list = list(map(int, input().strip()))
    bomb_list = list(map(str, input().strip()))
    
    checker = True
    while checker:
        temp = bomb_list.copy()
        for i in range(n):
            check_bomb(i, num_list[i], n)
            # print(bomb_list)
        if temp == bomb_list:
            checker = False
    for i in range(n):
        max_bomb(i, num_list[i], n)
        # print(bomb_list)
    print(bomb_list.count('*'))