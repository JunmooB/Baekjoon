import sys
input = sys.stdin.readline

def cal_odd_even(nums, zeros):
    length = len(nums)
    result = 0
    if length % 2 == 0:
        for i in range(length//2):
            if nums[2*i] == 1 or nums[2*i + 1] == 1:
                result += nums[2*i]
                result += nums[2*i + 1]
            else:
                result += nums[2*i] * nums[2*i +1]
    else:
        for i in range((length-1)//2):
            if nums[2*i] == 1 or nums[2*i + 1] == 1:
                result += nums[2*i]
                result += nums[2*i + 1]
            else:
                result += nums[2*i] * nums[2*i +1]
        if nums[length-1] > 0:
            result += nums[length-1]
        else:
            if len(zeros) == 0:
                result += nums[length-1]
    return result
        


n = int(input())
zeros, pos_nums, neg_nums = [], [], []
res = 0
for _ in range(n):
    temp = int(input())
    if temp > 0 :
        pos_nums.append(temp)
    elif temp < 0 :
        neg_nums.append(temp)
    else:
        zeros.append(temp)

pos_nums.sort(reverse=True)
neg_nums.sort()

res += cal_odd_even(pos_nums, zeros)
res += cal_odd_even(neg_nums, zeros)
print(res)