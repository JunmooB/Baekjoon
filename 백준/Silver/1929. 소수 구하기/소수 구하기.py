import sys
input = sys.stdin.readline

def search_primeNum(num):
    global res
    if num == 1:
        return
    elif num== 2:
        print(num)
    else:
        checker = False
        for i in range(2, round(num**(1/2)) + 1):
            if num % i == 0:
                checker = True
                break
        if not checker:
            print(num)

n , m = map(int, input().split()) 
for cnt in range(n,m+1):
    search_primeNum(cnt)