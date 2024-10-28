import sys
input = sys.stdin.readline

def binary_search():
    res_list =[]
    res_cnt = int(4e9)
    for i in range(n-2):
        s = i + 1
        e = n - 1
        refer = nums[i]
        while s < e:
            solution = refer + nums[s] + nums[e]
            if abs(solution) < abs(res_cnt):
                res_cnt = refer + nums[s] + nums[e]
                res_list = [refer, nums[s], nums[e]]
            
            if solution > 0:
                e = e - 1
            elif solution < 0:
                s = s + 1
            else:
                print(*res_list)
                exit()
    return res_list
    
if __name__ == '__main__':
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    
    res = binary_search()
    print(*res)