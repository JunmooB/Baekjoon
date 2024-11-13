import sys
input = sys.stdin.readline

import re

expression = str(input())

numbers = re.findall(r'\d+', expression)
numbers = [int(num) for num in numbers]  # 정수로 변환

operators = re.findall(r'[+\-*/]', expression)

res = numbers[0]
checker = False
for i in range(len(operators)):
    if operators[i] == '-': checker = True
    if checker:
        res -= numbers[i+1]
    else:
        res += numbers[i+1]
print(res)   