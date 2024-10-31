import sys
input = sys.stdin.readline

def binary_search():
    s = 0
    e = n-1
    l1 , l2 = 0 , 0
    checker = False
    while s<e:
        val = legos[s] + legos[e]
        if x > val:
            s += 1
        elif x < val:
            e -= 1
        else:
            l1 , l2 = legos[s] , legos[e]
            checker = True
            break            
    if checker:
        print("yes", l1, l2)
    else:
        print("danger")

# 1cm = 10 mm = 10,000 um = 10,000,000 nm
while True:
    try:
        x = int(input()) * int(1e7)
        n = int(input())
        legos = []
        for i in range(n):
            legos.append(int(input()))
        legos.sort()
        binary_search()
    except:
        break