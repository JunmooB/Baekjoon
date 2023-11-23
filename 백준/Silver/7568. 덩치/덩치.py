import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
results = []
for person in people:
    cnt =1
    for extra in people:
        if (person[0] < extra[0]) and (person[1] < extra[1]):
            cnt += 1
    results.append(cnt)

for result in results:
    print(result, end=' ')