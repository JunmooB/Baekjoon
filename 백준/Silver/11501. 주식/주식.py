import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    stocks.reverse()
    result = 0 
    Max = stocks[0]
    for stock in stocks:
        if Max < stock:
            Max = stock
        else:
            result += Max -stock
            
    print(result)