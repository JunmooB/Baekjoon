import sys
input = sys.stdin.readline

n = int(input())
works = []
total_work_time = 0
for _ in range(n):
    t , s = map(int, input().split())
    total_work_time += t
    works.append((t, s))
works.sort(key=lambda x: x[1])
last_time = works[-1][1]


# 1,000 * 1,000,000 O(N2)
# 총 걸리는 시간 > 제일 마지막시간  ->불가능
# 마지막 시간 - 총 걸리는 시간 부터 0까지
if total_work_time > last_time:
    print(-1)
    quit()
    
start_time = last_time - total_work_time
while start_time >= 0 :
    now_time = start_time
    for time , end_time in works:
        if now_time + time > end_time:
            start_time-=1
            break
        else:
            now_time += time
    if start_time + total_work_time == now_time:
        print(start_time)
        quit()
print(-1)