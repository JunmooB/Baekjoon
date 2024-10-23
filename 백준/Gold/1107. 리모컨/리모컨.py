import sys
input = sys.stdin.readline

from itertools import combinations, permutations, product

n = int(input())
m = int(input())
buttons = list(range(10))
if m:
    removes = list(map(int, input().split()))
    for remove in removes:
        buttons.remove(remove)

res = abs(n-100)
if m == 0:
    res = min(res, len(str(n)))
    print(res)
else:
    if n>= 10:
        permu_list = list(product(buttons, repeat=len(str(n))-1)) + list(product(buttons, repeat=len(str(n)))) + list(product(buttons, repeat=len(str(n))+1))
    elif n >= 100000:
        permu_list = list(product(buttons, repeat=len(str(n))-1)) + list(product(buttons, repeat=len(str(n))))
    else:
        permu_list = list(product(buttons, repeat=len(str(n)))) + list(product(buttons, repeat=len(str(n))+1))
    for permu in permu_list:
        temp = ''
        for num in permu:
            temp += str(num)
        temp =int(temp)
        if temp > int(1e6): break
        length = len(str(temp))
        temp_res = abs(n-temp) + length
        res = min(res, temp_res)

    print(res)