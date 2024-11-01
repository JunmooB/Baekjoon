import sys
input = sys.stdin.readline

import math

def healing_him(now_atk, now_hp, atk_plus, hp_plus):
    now_atk += atk_plus
    now_hp += hp_plus
    if now_hp > max_hp:
        now_hp = max_hp
    
    return now_atk, now_hp

def fight_monster(now_atk, now_hp, monster_atk, monster_hp):
    cnt = math.ceil(monster_hp / now_atk) 
    now_hp -= (cnt-1) * monster_atk
    return now_hp


n , initial_him_atk = map(int, input().split())
room_list = []
for i in range(n):
    checker , atk, hp = map(int, input().split())
    room_list.append([checker, atk, hp])

s = 1
e = n * int(1e12)
res = 0
while s<=e:
    max_hp = (s + e) // 2
    now_hp = max_hp
    him_atk = initial_him_atk
    for room in room_list:
        checker , atk, hp = room
        if checker == 1:
            now_hp = fight_monster(him_atk, now_hp, atk, hp)
            if now_hp <= 0:
                s = max_hp + 1
                break
        elif checker == 2:
            him_atk, now_hp = healing_him(him_atk, now_hp, atk, hp)
    if now_hp > 0:
        res = max_hp
        e = max_hp -1
print(res)