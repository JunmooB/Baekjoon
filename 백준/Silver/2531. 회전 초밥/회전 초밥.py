import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
table = []
for _ in range(n):
    table.append(int(input()))
for i in range(k-1):
    table.append(table[i])

result = 0
for i in range(n):
    temp = table[i:i+k]
    temp.append(c)
    cnt = len(set(temp))
    if cnt > result:
        result = cnt
print(result)