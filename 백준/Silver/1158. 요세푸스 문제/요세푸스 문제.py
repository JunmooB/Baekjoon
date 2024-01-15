import sys
input = sys.stdin.readline

n , k = map(int, input().split())
yose_nums = [ _ for _ in range(1, n+1)]

ind = k - 1
results = []
while yose_nums:
    length = len(yose_nums)
    if ind < length:
        pass
    else:
        ind %= length    
    results.append(yose_nums[ind])
    del yose_nums[ind]
    ind += k - 1

print("<", end='')
for i in range(len(results)-1):
    print(results[i], end='')
    print("," , end=' ')
print(results[len(results)-1], end='')
print(">")