import sys
input = sys.stdin.readline

n , k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
rank = 1

for medal in medals:
    if medal[0] == k:
        gold = medal[1]
        silver = medal[2]
        bronze = medal[3]
        medals.remove(medal)
        break

for medal in medals:
    if medal[1] > gold:
        rank += 1
        continue
    elif medal[1] == gold:            
        if medal[2] > silver:
            rank += 1
            continue
        elif medal[2] == silver:            
            if medal[3] > bronze:
                rank += 1
                continue
print(rank)