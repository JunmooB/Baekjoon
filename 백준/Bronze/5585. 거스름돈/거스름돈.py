import sys
input = sys.stdin.readline

n = int(input())
n = 1000-n
coins = [500, 100, 50, 10, 5]
result = 0

for coin in coins:    
    result += n // coin
    n -= (n // coin) * coin
result += n
print(result)