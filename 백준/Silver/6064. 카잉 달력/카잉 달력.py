import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M , N , x, y = map(int, input().split())
    k = x
    ans = 0 
    while k <= M * N:
        if (k-x) % M == 0 and (k-y) % N == 0 :
            ans = k
            break   
        k += M
    if ans:
        print(ans)
    else:
        print(-1)