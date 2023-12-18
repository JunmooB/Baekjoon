import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
students.sort()

result = 1e9
for i in range(n):
    ability = students[i] + students[2*n -1 -i]
    if ability < result :
        result = ability
print(result)