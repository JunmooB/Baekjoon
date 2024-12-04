import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n , m = map(int, input().split())
    books = [False] * (n+1)
    apply_for_books = []
    for _ in range(m):
        a , b = map(int, input().split())
        apply_for_books.append(( a, b))

    apply_for_books.sort(key=lambda x: x[1])
    for start , end in apply_for_books:
        for ind in range(start, end+1):
            if not books[ind]:
                books[ind] = True
                break
    res = books.count(True)
    print(res)