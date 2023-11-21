import sys
input = sys.stdin.readline


n = int(input())
Min, Max = 2 ,7
cnt = 1
while True:
    if n == 1:
        print(1)
        break
    else:
        if (n>=Min) and (n<=Max):
            print(cnt + 1)
            break
        else:
            Min +=  (6 * (cnt))
            Max +=  (6 * (cnt+1))
        cnt += 1