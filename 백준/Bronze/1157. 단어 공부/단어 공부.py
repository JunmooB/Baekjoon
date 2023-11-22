import sys
input = sys.stdin.readline

import operator

word = str(input())
cnt_list ={}

for k in range(len(word)-1):
    al = word[k]
    al = al.upper()
    if not al in cnt_list:
        cnt_list[al] = 1
    else:
        cnt_list[al] += 1


cnt_list_sort = sorted(cnt_list.items(), key=operator.itemgetter(1), reverse=True)

result_num = 0
result = ''
for cnt in cnt_list_sort:
    cnt_key = cnt[0]
    cnt_val = cnt[1]
    if cnt_val > result_num:
        result_num = cnt_val
        result = cnt_key
    elif cnt_val == result_num:
        result = '?'
        break
    else:
        break

print(result)