import sys
input = sys.stdin.readline

p , m = map(int, input().split())
# 방 리스트
# 방 리스트에 대한 점수
level_list = []
room_list = [[]]
max_list = []

for _ in range(p):
    level, name = input().split()
    if len(level_list) == 0:
        level_list.append([int(level)-10, int(level)+10])
        room_list[0].append([level, name])
        max_list.append(1)
    else:
        checker = False
        for i in range(len(level_list)):
            if level_list[i][0]<= int(level) <= level_list[i][1]:
                if max_list[i] < m:
                    room_list[i].append([level, name])
                    max_list[i] += 1
                    checker = True
                    break
        if not checker:
            level_list.append([int(level)-10, int(level)+10])
            room_list.append([[level, name]])
            max_list.append(1)

for i in range(len(max_list)):
    if max_list[i] == m:
        print("Started!")
    else:
        print("Waiting!")

    rooms = sorted(room_list[i], key=lambda x: [x[1]])
    for room in rooms:
        print(room[0], room[1])