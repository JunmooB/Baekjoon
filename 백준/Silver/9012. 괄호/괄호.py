import sys
input = sys.stdin.readline

def check_vps(string_list):
    length = len(string_list)
    for _ in range(length//2 +1):
        for i in range(len(string_list) -1):
            if string_list[i] == '(' and string_list[i+1] == ')':
                del string_list[i+1]
                del string_list[i]
                break

        

t = int(input())
for case in range(t):
    string_list = list(map(str, input().strip()))
    check_vps(string_list)
    if string_list :
        print("NO")
    else:
        print("YES")