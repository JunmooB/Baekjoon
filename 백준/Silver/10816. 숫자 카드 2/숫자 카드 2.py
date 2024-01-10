import sys
input = sys.stdin.readline

n = int(input())
dict = {}
inputs = list(map(int, input().split()))
n_out = int(input())
outputs = list(map(int, input().split()))

for input in inputs:
    if input in dict:
        dict[input] += 1
    else:
        dict[input] = 1


for output in outputs:
    if output in dict:
        print(dict[output], end=' ')
    else:
        print(0, end=' ')