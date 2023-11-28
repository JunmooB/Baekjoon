import sys
input = sys.stdin.readline

n , x = map(int, input().split())
visits = list(map(int, input().split()))

if sum(visits) == 0:
    print("SAD")
else:
    window = sum(visits[:x])
    maximum = window
    cnt = 1
    for i in range(x, n):
        window += visits[i] - visits[i-x]

        if maximum < window :
            maximum = window
            cnt = 1
        elif maximum == window:
            cnt += 1
    print(maximum)
    print(cnt)