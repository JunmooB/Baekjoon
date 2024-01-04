import sys
input = sys.stdin.readline

from collections import deque

def function(deque, command):
    if command[:4] == 'push':
        command , num = command.split()
        deque.append(num)
    elif command == 'top':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])
    elif command == 'pop':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    return deque

n = int(input())
q = deque()
for _ in range(n):
    command = str(input().strip())
    q = function(q, command)