import sys
input = sys.stdin.readline

h , w , n , m = list(map(int, input().split()))

h_cnt = ((h-1) // (n+1)) + 1
w_cnt = ((w-1) // (m+1)) + 1

result = h_cnt * w_cnt

print(result)