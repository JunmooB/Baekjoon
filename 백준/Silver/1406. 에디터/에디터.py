import sys
input = sys.stdin.readline

st1 = list(map(str, input().strip()))
st2 = []
m = int(input())

for _ in range(m):
    command = input().strip()
    if len(command) == 1:
        if command == 'L' :
            if st1:
                st2.append(st1.pop())
        elif command == 'D' :
            if st2:
                st1.append(st2.pop())
        else:
            if st1:
                st1.pop()
            
    else:
        st1.append(command[2])
st2.reverse()
result = st1 + st2
print(''.join(result))