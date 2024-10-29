import sys
input = sys.stdin.readline

m , n , l = map(int, input().split())
shots = sorted(list(map(int, input().split())))
animals = []
for i in range(n):
    a , b = map(int, input().split())
    animals.append((a, b))

res = 0
for animal in animals:
    x , y = animal[0] , animal[1]
    if y > l: continue
    Min = x - (l-y)
    Max = x + (l-y)
    s = 0
    e = m-1
    while s <= e:
        mid = (s+e) // 2
        if Min<=shots[mid]<=Max:
            res += 1            
            break
        elif shots[mid] < Min:
            s = mid +1
        elif shots[mid] > Max:
            e = mid - 1
print(res)