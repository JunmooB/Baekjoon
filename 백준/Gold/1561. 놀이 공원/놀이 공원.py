import sys
input = sys.stdin.readline

n , m = map(int, input().split())
# 걸리는 시간을 먼저 구하고 생각
rides = list(map(int, input().split()))
res = 0
# time
s = 1
e = int(1e12) + 1
time = None
while s<=e:
    mid = (s+e) // 2
    cnt = 0
    for ride in rides:
        cnt += mid // ride
        if mid % ride != 0: cnt +=1
    if cnt >= n:
        time = mid
        e = mid - 1
    elif cnt < n:
        s = mid + 1
# 직전까지
peoples = 0
before_rides = []
for i in range(m):
    peoples += (time-1) // rides[i]
    if (time-1) % rides[i] != 0: peoples +=1
    before_rides.append((time-1) % rides[i])
    
for i in range(m):
    if before_rides[i] == 0: peoples += 1
    if peoples == n:
        print(i+1)
        break