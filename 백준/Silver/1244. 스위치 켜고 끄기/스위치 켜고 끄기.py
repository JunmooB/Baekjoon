import sys
input = sys.stdin.readline

n = int(input())
switch_list = list(map(int, input().split()))
stu_num = int(input())
stu_list = [list(map(int, input().split())) for _ in range (stu_num)] # 1 남학생, 2 여학생

for stu in stu_list:
    # 남학생
    if stu[0] == 1:
        num = stu[1]
        for i in range(len(switch_list)):
            if (i+1) % num == 0:
                if switch_list[i] == 0:
                    switch_list[i] =1
                else:
                    switch_list[i] = 0
    # 여학생
    else:
        num = stu[1]
        ind = num -1
        cnt = 1
        while True:
            if (ind -cnt) >=0 and (ind + cnt) < n:
                if switch_list[ind-cnt] == switch_list[ind + cnt]:
                    cnt += 1
                else:
                    break
            else:
                break
        cnt_range = cnt -1
        for i in range(ind- cnt_range, ind+cnt_range+1):
            if switch_list[i] == 0:                    
                switch_list[i] =1
            else:
                switch_list[i] = 0
for i in range(len(switch_list)):
    print(switch_list[i], end=" ")
    if (i+1) % 20 == 0 :
        print()