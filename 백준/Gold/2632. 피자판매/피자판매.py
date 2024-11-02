import sys
input = sys.stdin.readline

from collections import defaultdict

def get_case_counts(pizza, length):
    case = defaultdict(int)
    for i in range(length):
        temp = pizza[i:] + pizza[:i]
        pre = 0
        for num in temp:
            pre += num
            case[pre] += 1
    case[sum(pizza)] = 1
    return case

target = int(input())
m , n = map(int, input().split())
a_list , b_list = [] , []
for _ in range(m): a_list.append(int(input()))
for _ in range(n): b_list.append(int(input()))
# a_list = a_list + a_list
# b_list = b_list + b_list


a_case = get_case_counts(a_list, m)
b_case = get_case_counts(b_list, n)

res = a_case.get(target, 0) + b_case.get(target, 0)
for num in a_case:
    if target-num in b_case:
        res += a_case[num] * b_case[target-num]
print(res)