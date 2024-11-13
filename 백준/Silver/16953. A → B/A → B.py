import sys
input = sys.stdin.readline

a , b = map(int, input().split())

res = 1
while True:
    if a == b:
        print(res)
        break
    else:
        if b % 2 == 0:
            b //= 2
            res += 1
        elif str(b)[-1] == '1' and len(str(b)) > 1 :
            b = int(str(b)[:-1])
            res += 1
        else:
            if a == b: print(res)
            else:
                print(-1)
                break