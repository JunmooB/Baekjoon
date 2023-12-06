import sys
input = sys.stdin.readline

n = int(input())
rods = []
for _ in range(n):
    L, H = map(int, input().split())
    rods.append([L,H])

rods.sort()
h_max = 0
idx = 0
for rod in rods:
    if rod[1] > h_max:
        h_max = rod[1]
        idx = rod[0]

result = h_max
h_now = rods[0][1]
l_now = rods[0][0]
for i in range(n):
    if rods[i][0] == idx:
        result += h_now * (rods[i][0] - l_now)
        break
    else:
        if rods[i][1] > h_now:
            result += h_now * (rods[i][0] - l_now)
            h_now = rods[i][1]
            l_now = rods[i][0]

h_now = rods[n-1][1]
l_now = rods[n-1][0] + 1
for i in range(n-1, -1 , -1):
    if rods[i][0] == idx:
        result += h_now * (l_now - rods[i][0] -1 )
        break
    else:
        if rods[i][1] > h_now:
            result += h_now * (l_now - rods[i][0] -1 )
            h_now = rods[i][1]
            l_now = rods[i][0] + 1


print(result)