import sys
input = sys.stdin.readline

n = int(input())
peoples = sorted(list(map(int, input().split())))

res = 0 
for i in range(n-2):
    refer = peoples[i]
    s = i + 1
    e = n-1
    while s < e:
        val = refer + peoples[s] + peoples[e]
        if val > 0:
            e = e - 1
        elif val < 0:
            s = s + 1
        else:
            if peoples[s] == peoples[e]:  # 중복되는 경우가 있을 때 처리
                count = e - s + 1
                res += (count * (count - 1)) // 2
                break
            else:
                left_count = 1
                right_count = 1
                while s + 1 < e and peoples[s] == peoples[s + 1]:
                    left_count += 1
                    s += 1
                while e - 1 > s and peoples[e] == peoples[e - 1]:
                    right_count += 1
                    e -= 1
                res += left_count * right_count
                s += 1
                e -= 1
            
print(res)