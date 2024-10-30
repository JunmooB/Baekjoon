import sys
input = sys.stdin.readline

n , m , l = map(int, input().split())
rests = sorted([0] + list(map(int, input().split())) + [l])

s = 1
e = l-1
res = 0
while s<=e:
    mid = (s+e) // 2
    cnt = 0
    
    for i in range(n+1):
        if rests[i+1] - rests[i] > mid:
            cnt +=(rests[i+1] - rests[i]-1) // mid 
    if cnt > m:
        s = mid + 1
    else:
        res = mid
        e = mid - 1
print(res)