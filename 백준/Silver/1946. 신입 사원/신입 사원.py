import sys
input = sys.stdin.readline

import heapq

t = int(input())

for __ in range(t):
    n = int(input())
    employees = []
    for _ in range(n):
        a, b = map(int, input().split())
        employees.append((a, b))
    employees.sort(key=lambda x : (x[0]))

    res_cnt = 0
    checker = employees[0][1]
    for i in range(1, n):
        if employees[i][1] < checker:
            checker = employees[i][1]
        else:
            res_cnt += 1
    print(n-res_cnt)