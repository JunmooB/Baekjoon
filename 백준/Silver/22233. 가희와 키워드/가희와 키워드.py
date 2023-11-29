import sys
input = sys.stdin.readline

n , m = map(int, input().split())
memos = {}
for _ in range(n):
    memos[input().strip()] = 1

result = n
for _ in range(m):
    temp = list(map(str, input().strip().split(',')))
    for te in temp:
        if te in memos.keys():
            if memos[te] == 1:
                memos[te] = 0
                result -= 1
    print(result)