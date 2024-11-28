import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# (A,F), (B,E), (C,D)
# 주사위 1개 -> 최대값 제외한 합

# 주사위 2개 -> 2면만 보이게, 3면만 보이게
    # 2면 : 4개
    # 3면 : 4개
# 주사위 3개 -> 2면만 보이게, 3면만 보이게, 한면만 보이게로 구성
    # 1면 : (n-2) * (n-1) * 4 + (n-2) * (n-2)
    # 2면 : 4 + (n-2) * 8
    # 3면 : 4 
num_list = []
for i in range(3):
    temp = min(nums[i], nums[5-i])
    num_list.append(temp)
num_list.sort()

if n == 1:
    print(sum(nums) - max(nums))
else:
    res = 0
    res += ((n-2) * (n-1) * 4 + (n-2) * (n-2)) * num_list[0]
    res += (4 + (n-2) * 8) * (num_list[0] + num_list[1])
    res += 4 * (sum(num_list))
    
    print(res)