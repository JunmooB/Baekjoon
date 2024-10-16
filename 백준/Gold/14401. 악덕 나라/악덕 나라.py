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
        
def is_point_on_segment(p, q, r):
    """
    선분 pq와 점 r이 주어졌을 때, 점 r이 선분 pq 위에 있는지 여부를 반환하는 함수.
    
    :param p: 첫 번째 점 (x1, y1)
    :param q: 두 번째 점 (x2, y2)
    :param r: 확인할 점 (xr, yr)
    :return: r이 선분 pq 위에 있으면 True, 그렇지 않으면 False
    """
    # 1. 점 r이 직선 pq 위에 있는지 확인 (세 점이 일직선상에 있는지 확인)
    if (q[0] - p[0]) * (r[1] - p[1]) != (q[1] - p[1]) * (r[0] - p[0]):
        return False

    # 2. 점 r이 선분 pq의 범위 내에 있는지 확인
    if min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1]):
        return True
    
    return False


n , m = map(int, input().split())
cities = [(0,0)]
for _ in range(n):
    x, y = map(int ,input().split())
    cities.append((x , y))
    
loads = set()
for _ in range(m):
    a, b = map(int, input().split())
    a, b = min(a,b) , max(a,b)
    loads.add((a,b))
    
cant_load = set()
# for i in range(1, n):
#     for j in range(i+1, n+1):
#         for k in range(1, n+1):
#             if i == k or j == k: continue
#             if is_point_on_segment(cities[i], cities[j], cities[k]):
#                 cant_load.add((i,j))

parent = list(range(n+1))
cnt = 0
edges = []
for i in range(1, n):
    for j in range(i+1, n+1):
        if (i,j) in cant_load: continue
        for k in range(1, n+1):
            if i == k or j == k: continue
            if is_point_on_segment(cities[i], cities[j], cities[k]):
                cant_load.add((i,j))
                break
        if (i,j) in loads:
            union_parent(i,j)
            cnt += 1
        elif (i,j) not in cant_load:        
            dist = (cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2
            edges.append((-dist, i, j))

edges.sort()
res = 0
for key , a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += -key
print(res)
            