import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
Max , Min = max(nums) , min(nums)

print(Max * Min)