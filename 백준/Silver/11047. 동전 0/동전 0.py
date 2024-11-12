import sys
input = sys.stdin.readline

n , k = map(int, input().split())
coins = []
for _ in range(n): coins.append(int(input()))
coins.sort(reverse=True)

res = 0 
for coin in coins:
    cnt = k // coin
    k -= cnt * coin
    res += cnt
    if k == 0: break
print(res)