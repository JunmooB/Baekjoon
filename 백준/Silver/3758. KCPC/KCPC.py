import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):    
    n , k , id, m = map(int, input().split())

    score_matrix = [[0]*(k+1) for __ in range(n+1)]
    submit_cnt_list = [0] * (n+1)
    submit_last_list = [0] * (n+1)

    time = 1
    for ___ in range(m):
        team, prob, score = map(int, input().split())
        submit_cnt_list[team] += 1
        submit_last_list[team] = time
        if score > score_matrix[team][prob]:
            score_matrix[team][prob] = score
        time += 1 

    team_score_list = []
    for team_score in score_matrix:
        team_score_list.append(sum(team_score))

    rank = 1
    for i in range(len(team_score_list)):
        if i == id:
            continue
        else:
            if team_score_list[i] > team_score_list[id]:
                rank += 1
            elif team_score_list[i] == team_score_list[id]:
                if submit_cnt_list[i] < submit_cnt_list[id]:
                    rank +=1
                elif submit_cnt_list[i] == submit_cnt_list[id]:
                    if submit_last_list[i] < submit_last_list[id]:
                        rank += 1
    print(rank)