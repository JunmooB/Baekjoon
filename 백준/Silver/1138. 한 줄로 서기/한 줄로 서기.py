import sys
input = sys.stdin.readline

n = int(input())
records = list(map(int, input().split()))
results = [0] * (n)

for i in range(n):
    person = i + 1
    cnt_higher = records[i]
    cnt = 0
    for j in range(n):
        if results[j] == 0:
            cnt += 1
        
        if cnt == cnt_higher + 1:
            results[j] = person
            break
for result in results:
    print(result, end = ' ')