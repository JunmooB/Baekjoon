import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    n , m = map(int, input().split())
    documents = list(map(int, input().split()))
    q_imp = deque(documents)
    q_ind = deque(i for i in range(n))
    cnt = 1
    while True:
        Max = max(q_imp)
        if q_imp[0] == Max:
            if q_ind[0] == m:
                print(cnt)
                break
            else:
                q_imp.popleft()
                q_ind.popleft()
                cnt += 1

        else:
            q_imp.append(q_imp.popleft())
            q_ind.append(q_ind.popleft())