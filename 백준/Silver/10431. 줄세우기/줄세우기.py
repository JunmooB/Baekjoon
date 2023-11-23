import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    input_peo = list(map(int , input().split()))
    number = input_peo[0]
    input_peo = input_peo[1:]

    sum_cnt = 0
    result_list = []
    result_list.append(input_peo[0])
    input_peo = input_peo[1:]


    for person in input_peo:
        for result in result_list:
            ind = result_list.index(result)
            if person < result:                
                result_list.insert(ind, person)
                sum_cnt += len(result_list[ind+1:])
                break
            if ind == len(result_list)-1:
                result_list.append(person)
                break
    print(number, sum_cnt)