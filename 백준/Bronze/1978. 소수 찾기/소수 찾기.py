import sys
input = sys.stdin.readline

def search_primeNum(num):
    global res
    if num == 1:
        return
    elif num== 2:
        res+=1
    else:
        checker = False
        for i in range(2, round(num**(1/2)) + 1):
            if num % i == 0:
                checker = True
                break
        if not checker:
            res+=1
                

n = int(input())
nums = list(map(int, input().split()))
res = 0
for num in nums:
    search_primeNum(num)
print(res)