import sys
input = sys.stdin.readline

s = int(input())

cnt = 0
i = 1
target = 0
while True:
    target += i
    cnt += 1
    if target == s:
        print(cnt)
        break
    elif s < target + i + 1:
        print(cnt)
        break
    
    i += 1