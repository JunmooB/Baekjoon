import sys
from itertools import combinations
input = sys.stdin.readline

people = []

def sort_num(x):
    return x

for i in range(9) :
    temp = int(input())
    people.append(temp)

case_list = list(combinations(people, 7))

for case in case_list :
    if sum(case) == 100 :
        temp = sorted(case, key=sort_num)
        for i in temp :
            print(i)
        break