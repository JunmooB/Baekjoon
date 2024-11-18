import sys
input = sys.stdin.readline

n = int(input())

string_cnt = {}
for _ in range(n):
    string = str(input().strip())
    length = len(string)
    for i, s in enumerate(string):
        if s in string_cnt:
            string_cnt[s]+= 10**(length-i - 1)
        else:
            string_cnt[s] = 10**(length-i - 1)

strings = sorted(string_cnt.items(), key=lambda item: item[1], reverse=True)
res = 0
num = 9
for _, cnt in strings:
    res += cnt * num
    num -= 1
     
print(res)