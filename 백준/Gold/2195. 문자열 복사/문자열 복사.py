import sys
input = sys.stdin.readline

S = str(input().strip())
P = str(input().strip())
left, right = 0, 1
length = len(P)
result = 0

if length == 1:
    print(1)
else:
    while True:
        if right == length :
            break
        if P[left:right] in S:
            if right + 1 == length:
                if P[left:right+1] in S:
                    result += 1
                else:
                    result += 2
                right += 1                
            else:
                if P[left:right+1] in S:
                    right += 1
                else:
                    left = right
                    right = right + 1
                    result += 1   

    print(result)