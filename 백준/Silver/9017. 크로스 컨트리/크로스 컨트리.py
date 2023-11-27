import sys
input = sys.stdin.readline

import operator

def find_value(dict, finding_value):
    res = []
    for key, value in dict.items():
        if value == finding_value:
            res.append(key)
    return res

t = int(input())
for i in range(t):
    n = int(input())
    rank_list = list(map(int, input().split()))
    
    j = 1
    team_list = []
    while True:
        if rank_list.count(j) == 0:
            break
        else:
            if rank_list.count(j) == 6:
                team_list.append(j)
        j += 1

    cnt = 1
    result = {}
    result_checker = {}
    for team in team_list:
        result[team] = 0
        result_checker[team] = 0

    for rank in rank_list:
        if rank in team_list:
            if result_checker[rank] < 4:
                result[rank] += cnt
                result_checker[rank] += 1
            cnt +=1
    min_by_value = min(result.items(), key=operator.itemgetter(1))
    # print("df", min_by_value)

    res = find_value(result, min_by_value[1])
    # print("우승리스트: ", res)
    if len(res) == 1:
        print(min_by_value[0])
    else:
        for team in res:
            result[team] = 0           

        for rank in rank_list:
            if rank in res:
                result[rank] += 1
                if result[rank] == 5:
                    print(rank)
                    break