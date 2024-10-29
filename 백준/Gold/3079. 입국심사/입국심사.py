import sys
input = sys.stdin.readline

def time_operator(time):
    cnt = 0
    for pas in pass_list:
        cnt += time // pas
    return cnt


n , m = map(int, input().split())
pass_list = []
for i in range(n):
    pass_list.append(int(input()))
s = 1
e = int(1e18)
res = 0
while s<= e:
    mid = (s+e) // 2
    key = time_operator(mid)
    if key >= m :
        res = mid
        e = mid -1
    else:
        s = mid + 1
print(res)