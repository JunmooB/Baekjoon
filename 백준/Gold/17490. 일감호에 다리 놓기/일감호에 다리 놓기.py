import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x , y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

edges = []

n , m , k = map(int, input().split())
parent = list(range(n+1))
s_list = list(map(int, input().split()))
for i, s in enumerate(s_list):
    edges.append((s, 0, i+1))
edges.sort()

remove_list = set()
for i in range(m):
    a, b = map(int, input().split())
    a, b = min(a,b), max(a,b)
    remove_list.add((a,b))
cnt = 0    
for i in range(1,n):
    if (i,i+1) not in remove_list:
        union_parent(i, i+1)
        cnt+=1
if (1, n) not in remove_list:
    union_parent(1,n)
    cnt+=1

rock_cnt = 0
for key, a, b in edges:
    if (a,b) in remove_list: continue
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cnt += 1
        rock_cnt += key
if cnt == n and rock_cnt <=k:
    print("YES")
elif m <= 1:
    print("YES")
else:
    print("NO")