import sys
input = sys.stdin.readline
def comparing_nums(new_num, num_list):
    if len(num_list) == 0:
        num_list.append(new_num)
    else:
        checker = False
        for i in range(len(num_list)):
            num = num_list[i]
            # case1 == (new_num + num)
            # case2 == (num + new_num)
            # case1 > case2인 경우 new_num이 앞
            case1 = str(new_num) + str(num)
            case2 = str(num) + str(new_num)
            if case1 > case2:
                num_list.insert(i, new_num)
                checker = True
                break
        
        if not checker:
            num_list.append(new_num)

k , n = map(int, input().split())
key = 0
checker_key = True
nums = [[] for _ in range(10)]
# res = ''

for _ in range(k):
    temp = int(input())
    index = int(str(temp)[0])

    comparing_nums(temp, nums[index])

    if temp > key:
        key = temp


for i in range(9,0,-1):
    if len(nums[i]) != 0:
        temp = ''
        for ele in nums[i]:
            if ele == key and checker_key:
                for _ in range(n-k+1):
                    temp += str(ele)
                checker_key = False
            else:
                temp += str(ele)
        print(temp, end='')