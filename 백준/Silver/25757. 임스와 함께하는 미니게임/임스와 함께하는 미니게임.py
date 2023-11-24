import sys
input = sys.stdin.readline

n , case = map(str, input().split())
# names = []
no_over_names = ['0'] * int(n)
ind = 0
for i in range(int(n)):
    temp = str(input())
    temp = temp[:-1]
    no_over_names[i] = temp
    # if not temp in no_over_names:
    #     no_over_names[ind] = temp
    #     # no_over_names.append(temp)
    #     ind += 1
no_over_names = set(no_over_names)

cnt = len(no_over_names)
if case == 'Y':    
    print(cnt // 1)
elif case =='F':
    print(cnt // 2)
else:
    print(cnt // 3)