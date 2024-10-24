import sys
input = sys.stdin.readline

def switch_num(num):
    res_list = [['0'] * (s+2) for _ in range(2*s + 3)]
    match num:        
        case 1:
            for i in range(2*s+3):
                for j in range(s+2):
                    if (0<i<s+1 or s+1<i <2*s +2) and j == s+2-1 :
                        res_list[i][j] = '|' 
        case 2:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and j == s+2-1 :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and j == 0 :
                        res_list[i][j] = '|' 
        case 3:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 or s+1<i <2*s +2) and j == s+2-1 :
                        res_list[i][j] = '|' 
        case 4:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==s+1 ) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0 or j == s+2-1) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and j == s+2-1 :
                        res_list[i][j] = '|' 
        case 5:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and j == s+2-1 :
                        res_list[i][j] = '|' 
        case 6:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and (j==0 or j == s+2-1) :
                        res_list[i][j] = '|' 
        case 7:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 ) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== s+2-1) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and (j == s+2-1) :
                        res_list[i][j] = '|' 
        case 8:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0 or j == s+2-1) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and (j==0 or j == s+2-1) :
                        res_list[i][j] = '|' 
        case 9:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or i==s+1 or i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0 or j == s+2-1) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and (j == s+2-1) :
                        res_list[i][j] = '|' 
        case 0:
            for i in range(2*s+3):
                for j in range(s+2):
                    if  (i==0 or  i == 2*(s+1)) and (j != 0 and j != s+1):
                        res_list[i][j] = '-'
                    if (0<i<s+1 ) and (j== 0 or j == s+2-1) :
                        res_list[i][j] = '|' 
                    if (s+1<i <2*s +2) and (j==0 or j == s+2-1) :
                        res_list[i][j] = '|' 
                        
            
            
            
            
    return res_list

s, n = map(int, input().split())
res_list = []
str_n = str(n)
for i in str_n:
    temp_list = switch_num(int(i))
    res_list.append(temp_list)
    
# 출력 처리
for i in range(2*s+3):
    for j in range(len(str_n)):
        for k in range(s+2):
            if res_list[j][i][k] == '0':
                print(' ', end='')
            else:
                print(res_list[j][i][k], end='')
        if j != len(str_n) - 1:  # 마지막 숫자가 아니면 공백 추가
            print(' ', end='')
    print()  # 줄바꿈