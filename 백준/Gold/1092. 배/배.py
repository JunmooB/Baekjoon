import sys
input = sys.stdin.readline

n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))

crains.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > crains[0]:
    print(-1)
    exit()

res = 0
for i in range(m):
    while boxs:
        for crain in crains:
            if not boxs or crain < boxs[-1]:
                continue
            for box in boxs:
                if crain >= box:
                    boxs.remove(box)
                    break
        res += 1
print(res)