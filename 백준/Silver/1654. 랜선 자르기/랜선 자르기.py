import sys
input = sys.stdin.readline

def cut_lan_line(lans, length):
    cnt = 0
    for lan in lans:
        cnt += (lan // length)
    return cnt



k , n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)

result = 0
while left <= right:    
    mid = (left+right) // 2
    cnt = cut_lan_line(lans, mid)
    if n <= cnt :
        left = mid +1
        if mid > result :
            result = mid
    else :
        right = mid - 1
print(result)