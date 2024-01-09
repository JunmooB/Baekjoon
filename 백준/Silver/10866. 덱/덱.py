import sys
input = sys.stdin.readline

from collections import deque

def function(deque, command):
    if command[:10] == 'push_front':
        command , num = command.split()
        deque.appendleft(num)
    elif command[:9] == 'push_back':
        command , num = command.split()
        deque.append(num)
    elif command == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif command == 'pop_back':
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
    elif command == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif command == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])


    return deque

n = int(input())
q = deque()
commands =[]
for _ in range(n):
    command = str(input().strip())
    commands.append(command)
for command in commands:    
    # print(q, end=' ')
    q = function(q, command)