import sys
input = sys.stdin.readline

def GCD(x, y):
    while (y):
        x , y = y , x % y
    return x
def LCM(x,y, gcd):
    result = (x*y)//gcd
    return result


a , b = map(int, input().split())
res1 = GCD(a,b)
res2 = LCM(a,b,res1)

print(res1)
print(res2)