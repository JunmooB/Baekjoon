import sys
input = sys.stdin.readline

from queue import PriorityQueue

pq = PriorityQueue()
res=0

n = int(input())
for i in range(n):
    num = int(input())
    pq.put(num)
    
while not pq.empty():
    if not pq.empty():
        left = pq.get()
    if not pq.empty():
        right = pq.get()
        res += left+right
        pq.put(left+right)
    else:
        print(res)