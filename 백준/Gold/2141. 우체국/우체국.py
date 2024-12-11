import sys
input = sys.stdin.readline

n = int(input())
people = []
sum_people = 0
for _ in range(n):
    loc , num = map(int ,input().split())
    people.append((loc, num))
    sum_people += num
mid_num = sum_people / 2
people.sort(key=lambda x: [x[0]])

temp_num = 0
for loc , num in people:
    temp_num += num
    if temp_num >= mid_num:
        print(loc)
        break