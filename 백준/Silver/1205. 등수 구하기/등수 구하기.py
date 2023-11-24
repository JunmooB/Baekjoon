import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())


if n == 0:
    print(1)
else:
    rank_list = list(map(int, input().split()))
    if n < p :
        cnt = 1
        for rank_score in rank_list:
            if score >= rank_score :
                break
            cnt += 1
        print(cnt)
    else: # n == p
        if min(rank_list) >= score:
            print(-1)
        else:
            cnt = 1
            for rank_score in rank_list:
                if score >= rank_score :
                    break
                cnt += 1
            print(cnt)