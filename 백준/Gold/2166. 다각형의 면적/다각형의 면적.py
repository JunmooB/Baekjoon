import sys
input = sys.stdin.readline

def polygon_area(arr_x , arr_y , poly_num):
    area = 0
    for i in range(poly_num):
        area += arr_x[i] * arr_y[i+1] - arr_x[i+1] * arr_y[i]        
    return  abs(area) / 2


n = int(input())
arr_x , arr_y = [] , []

for i in range(n):
    temp_x , temp_y = map(int, input().split())
    arr_x.append(temp_x)
    arr_y.append(temp_y)

# 첫번째 값 마지막에 추가
arr_x.append(arr_x[0])
arr_y.append(arr_y[0])

res = polygon_area(arr_x, arr_y, n)
print(res)