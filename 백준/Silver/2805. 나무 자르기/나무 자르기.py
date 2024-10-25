import sys
input = sys.stdin.readline

def cal_tree(num):
    cnt = 0
    for tree in trees:
        temp_cnt = tree - num
        if temp_cnt > 0:
            cnt += temp_cnt
    return cnt


n , m = map(int, input().split())
trees = list(map(int, input().split()))
Max = max(trees)

start = 0
end = Max
res = 0
while start<=end:
    mid = (start+end) // 2
    if cal_tree(mid) >= m:
        if mid > res:
            res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)