import sys
input = sys.stdin.readline

n = int(input())
plus , minus = [] , []
res = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
       res += 1
    else:
        minus.append(num)
plus.sort(reverse=True)
minus.sort()

len_plus, len_minus = len(plus), len(minus)

for i in range(0, len_plus, 2):
    if i + 1 == len_plus:
        res += plus[i]
    else:
        res += plus[i] * plus[i+1]

for i in range(0, len_minus, 2):
    if i + 1 == len_minus:
        res += minus[i]
    else:
        res += minus[i] * minus[i+1]   
    
print(res)