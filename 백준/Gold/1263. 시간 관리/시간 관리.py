import sys
input = sys.stdin.readline

n = int(input())
works = []

for _ in range(n):
    t, s = map(int, input().split())
    works.append((t, s))

# 작업을 마감 시간이 빠른 순으로 정렬
works.sort(key=lambda x: x[1])

# 마지막 시간에서 거꾸로 계산
current_time = works[-1][1]

for t, s in reversed(works):
    # 작업이 가능한 가장 늦은 시작 시간을 갱신
    current_time = min(current_time, s) - t
    if current_time < 0:
        print(-1)
        exit()

print(current_time)
