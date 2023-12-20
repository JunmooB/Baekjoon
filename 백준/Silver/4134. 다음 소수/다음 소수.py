import sys
input = sys.stdin.readline

def find_primeNum(num):
    while True:
        temp = True        
        for j in range(2, int(num**(1/2)) + 1):
            if (num % j) == 0:
                temp = False
                break
        if temp :
            return num
        num += 1

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0 or num == 1:
        print(2)
    else:
        result = find_primeNum(num)
        print(result)