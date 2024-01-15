import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    functions = list(map(str, input().strip()))
    n = int(input())
    arr = str(input().strip())
    arr = arr.replace('[','')
    arr = arr.replace(']', '')

    checker = True
    if arr :
        arr = deque(list(map(int, arr.split(','))))
    else:
        arr = deque([])

    left_right = True
    cnt = functions.count("R")
    for function in functions:
        if function == 'R':
            if left_right == True:
                left_right = False
            else:
                left_right = True
        elif function == 'D':
            if arr:
                if left_right:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                checker = False
                break
    if cnt % 2 == 1:
        arr.reverse()
        
    if checker:
        if len(arr) >= 2:
            print("[", end='')
            for i in range(len(arr)-1):
                print(arr[i], end='')
                print("," , end='')
            print(arr[len(arr)-1], end='')
            print("]")
        elif len(arr) == 1:
            print("[" + str(arr[0]) + "]")
        else:
            print("[]")
    else:
        print("error")