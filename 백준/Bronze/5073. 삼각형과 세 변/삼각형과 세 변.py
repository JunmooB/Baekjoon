import sys
input = sys.stdin.readline

def solution(a, b, c):
    temp = [a, b, c]
    temp.sort(reverse = True)
    return temp

while True:
    a, b, c = list(map(int, input().split()))
    
    if (a == 0) and (b == 0) and (c == 0):
        break
    else:
        tri_num = solution(a, b, c)
        if tri_num[0] >= tri_num[1] + tri_num[2]:
            print("Invalid")
        elif (tri_num[0] == tri_num[1]) and (tri_num[1] == tri_num[2]):
            print("Equilateral")
        elif (tri_num[0] == tri_num[1]) or (tri_num[1] == tri_num[2]):
            print("Isosceles")
        elif (tri_num[0] != tri_num[1]) and (tri_num[1] != tri_num[2]):
            print("Scalene")        
