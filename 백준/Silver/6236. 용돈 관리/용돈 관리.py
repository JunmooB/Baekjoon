import sys
input = sys.stdin.readline

n , m = map(int, input().split())
money_list = []
start , end = int(1e9), 0
for i in range(n):
    temp = int(input())
    if start > temp: start = temp
    end += temp
    money_list.append(temp)

res = 0
while start <= end:
    mid = (start + end) // 2
    now_money = mid
    cnt = 1
    checker = False
    for money in money_list:
        if mid < money:
            start = mid + 1
            checker = True
            break
        else:
            if now_money - money < 0:
                cnt += 1
                now_money = mid -money
            else:
                now_money -= money
    if checker: continue
    if cnt <= m:
        end = mid - 1
        res = mid
    elif cnt > m :
        start = mid + 1 
    
print(res)