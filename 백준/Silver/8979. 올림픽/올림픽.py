import sys
input = sys.stdin.readline

n , k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]

rank_list = []
results = sorted(medals, key = lambda x:[-x[1], -x[2], -x[3]])
rank = 1
for i in range(len(results) -1):
    cnt = 1
    while True:
        if results[i][1] == results[i+cnt][1]:
            if results[i][2] == results[i+cnt][2]:
                if results[i][3] == results[i+cnt][3]:
                    cnt += 1
                else:
                    break
            else:
                break
        else:
            break
    for j in range(cnt):
        rank_list.append(rank)
    rank += cnt

for result in results:
    if result[0] == k:
        ind = results.index(result)
        break
print(rank_list[ind-1])