import sys
input = sys.stdin.readline

n , k = map(int, input().split())
hambergers = list(map(str, input().strip()))
checkers = []
for hamberger in hambergers:
    if hamberger == 'H':
        checkers.append(1)
    else:
        checkers.append(0)

result = 0
for i in range(n):
    if hambergers[i] == 'P':
        for j in range(-k, k+1):
            if 0<= i+j <n and checkers[i+j] == 1:
                checkers[i+j] =0
                result += 1
                break

print(result)