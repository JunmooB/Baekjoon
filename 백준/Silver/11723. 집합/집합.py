import sys
input = sys.stdin.readline

n = int(input())
set_list = []

def string_split(string):
    if string[:2] == 'al' or string[:2] == 'em':
        return string, -1, False
    else:
        string , x = string.split()
        return string, x, True


def func_oper_num(operation, x, set_list):
    x = int(x)
    if operation == 'add':
        if not x in set_list:
            set_list.append(x)
    elif operation == 'remove':
        if x in set_list:
            set_list.remove(x)
    elif operation == 'check' :
        if x in set_list:
            print(1)
        else:
            print(0)
    elif operation == 'toggle' :
        if not x in set_list:
            set_list.append(x)
        else:
            set_list.remove(x)    

    return set_list

def func_oper(operation, set_list):
    operation = operation[:len(operation)-1]
    if operation == 'all':
        set_list = list(range(1,21))
    else:
        set_list = []
    return set_list

for i in range(n):
    string = str(input())
    operation , x, checker = string_split(string)
    if checker:
        set_list = func_oper_num(operation, x, set_list)  
    else:
        set_list = func_oper(operation, set_list)