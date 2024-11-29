import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

# 양수/음수 분리 및 정렬
pos = sorted([book for book in books if book > 0], reverse=True)
neg = sorted([book for book in books if book < 0])

# 가장 멀리 있는 책 거리
max_distance = 0
if pos and neg:
    max_distance = max(abs(pos[0]), abs(neg[0]))
elif pos:
    max_distance = pos[0]
elif neg:
    max_distance = abs(neg[0])

# 그룹별 거리 합산
def calculate_distance(locations):
    distance = 0
    for i in range(0, len(locations), m):
        distance += abs(locations[i])  # 각 그룹의 가장 먼 책만 방문
    return distance

# 왕복 거리 계산 후 가장 먼 거리 제외
res = calculate_distance(pos) + calculate_distance(neg)
print(res * 2 - max_distance)
