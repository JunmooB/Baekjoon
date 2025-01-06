import sys
input = sys.stdin.readline

n = int(input())
num = str(input().strip())
res = 0
for digit in num:
    res += int(digit)
print(res)