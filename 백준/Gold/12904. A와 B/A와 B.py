import sys
input = sys.stdin.readline

s = str(input().strip())
t = str(input().strip())

length = len(t) - len(s)
res_list = [t]
for i in range(length):
    temp_list = []
    for st in res_list:
        if st[-1] == 'A':
            temp_list.append(st[:-1])
        else:
            temp_list.append(st[:-1][::-1])
    res_list = temp_list
if s in res_list:
    print(1)
else:
    print(0)