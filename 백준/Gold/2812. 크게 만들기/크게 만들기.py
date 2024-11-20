import sys
input = sys.stdin.readline

n , k = map(int, input().split())
nums = list(map(int, input().strip()))

stack = [nums[0]]
for i in range(1, len(nums)):
    while stack and k > 0:
        if stack[-1] < nums[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(nums[i])

if k > 0:
    print(*stack[:-k], sep = '', end ='')
else:
    print(*stack, sep = '', end ='')