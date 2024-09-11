import sys
input = sys.stdin.readline

from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()
res=[]
for i in range(n):
    num = int(input())
    if num == 0:
        if pq.empty():
            res.append(0)
        else:
            priority , value = pq.get()
            res.append(value)
    else:
        pq.put((abs(num), num))

for r in res:
    print(r)