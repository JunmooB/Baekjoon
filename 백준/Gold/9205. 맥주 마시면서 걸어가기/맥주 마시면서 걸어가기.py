import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    locations = []
    visited = [0] * (n+2)
    start_x, start_y = map(int, input().split())
    for i in range(n+1):
        x , y = map(int, input().split())
        locations.append([x, y])
    q = deque([[start_x, start_y]])
    visited[0] = 1
    checker = False
    while q:
        x , y = q.popleft()
        if x == locations[n][0] and y == locations[n][1]:
            print("happy")
            checker = True
        for ind, location in enumerate(locations):
            if visited[ind+1] == 0:
                if abs(x - location[0]) + abs(y - location[1]) <=1000:
                    visited[ind+1] = 1
                    q.append([location[0], location[1]])
    if not checker:
        print("sad")