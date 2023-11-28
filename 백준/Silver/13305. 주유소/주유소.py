import sys
input = sys.stdin.readline

n = int(input())
length_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))

result = 0
while True:    
    if len(price_list) == 0:
        print(result)
        break
    elif len(price_list) == 1:
        result += length_list[0] * price_list[0]
        print(result)
        break
    else:
        low_price = min(price_list)
        ind = price_list.index(low_price)
        
        re = len(price_list) - ind - 1

        result += low_price * sum(length_list[ind:])

        price_list = price_list[:ind]
        length_list = length_list[:ind]