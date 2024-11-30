import sys
input = sys.stdin.readline

n = int(input())
projects = []
for i in range(n):
    day , score = map(int, input().split())
    projects.append((day, score))
max_day = max(projects, key=lambda x: x[0])[0]
assign_day = [0] * (max_day + 1)

projects.sort(key=lambda x : [-x[1], x[0]])
for day, score in projects:
    for i in range(day, 0, -1):
        if not assign_day[i]:
            assign_day[i] = score
            break
print(sum(assign_day))