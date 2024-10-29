import sys
input = sys.stdin.readline

def snack_operator(bar_len):
    cnt = 0
    for snack in snacks:
        cnt += snack // bar_len
    return cnt


m, n = map(int, input().split())
snacks = list(map(int, input().split()))

s = 1
e = int(1e9)
res = 0
while s<= e:
    mid = (s+e) // 2
    key = snack_operator(mid)
    if key >= m :
        res = mid
        s= mid + 1
    else:
        e = mid -1
print(res)