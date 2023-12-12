import sys
input = sys.stdin.readline

test = str(input().strip())

result = 1
while test:
    str_i = str(result)
    for i in range(len(str_i)):
        if test == '':
            break
        else:
            if str_i[i] == test[0]:
                test = test[1:]
    result += 1
    
print(result-1)