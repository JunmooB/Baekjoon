import sys
input = sys.stdin.readline

import heapq

n = int(input())
quiz = []
for _ in range(n):
    deadline , cup_ramyun = map(int, input().split())
    quiz.append((deadline, cup_ramyun))
quiz.sort()

hp = []
for deadline, cup_ramyun in quiz:
    heapq.heappush(hp, cup_ramyun)
    # print("push", deadline, cup_ramyun)
    if len(hp) > deadline:        
        heapq.heappop(hp)
        # print("pop", deadline, cup_ramyun, hp)
print(sum(hp))