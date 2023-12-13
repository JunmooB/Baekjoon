import sys
input = sys.stdin.readline

from collections import deque, defaultdict

n , k = map(int, input().split())
num_list = list(map(int, input().split()))

result = 0
checker = deque([])
dic = defaultdict(int)
for num in num_list:
    if dic[num] == k:
        if result < len(checker):
            result = len(checker)
        while True:
            temp = checker.popleft()
            dic[temp] -= 1
            if temp == num:
                checker.append(temp)
                dic[temp] += 1
                break
    else:
        checker.append(num)
        dic[num] += 1

if result < len(checker):
    result = len(checker)
print(result)