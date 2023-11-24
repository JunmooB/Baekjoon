import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input()))[:-1] for _ in range(n)]

breaker = True
for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            heart_row = i +1
            heart_col = j
            print(i+2, j+1)
            breaker = False
            break
    if not breaker:
        break
# 왼쪽 팔
left_arm = 0
for j in range(heart_col-1, -1, -1):
    if graph[heart_row][j] == '_':
        break
    left_arm += 1


# 오른쪽 팔
right_arm = 0
for j in range(heart_col+1, n):
    if graph[heart_row][j] == '_':
        break
    right_arm += 1

# 허리
waist = 0
for i in range(heart_row +1, n):
    if graph[i][heart_col] == '_':
        break
    waist += 1

# 왼쪽 다리
left_leg = 0
for i in range(heart_row + waist +1, n):
    if graph[i][heart_col -1] == '_':
        break
    left_leg +=1

# 오른쪽 다리

right_leg = 0
for i in range(heart_row + waist +1, n):
    if graph[i][heart_col + 1] == '_':
        break
    right_leg +=1

print(left_arm, right_arm, waist, left_leg, right_leg)