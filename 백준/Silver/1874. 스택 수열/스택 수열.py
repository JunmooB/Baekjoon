import sys
input = sys.stdin.readline

n = int(input())
stack = []
ind = 1
res = []
checker = True
for i in range(n):
    num = int(input())
    while ind <= num:
        stack.append(ind)
        ind+=1
        res.append("+")
        
    length = len(stack)
    if stack[length-1] == num:
        res.append("-")
        stack.pop()
    else:        
        checker = False
        break
        
if checker:
    for re in res:
        print(re)
else:
    print("NO")