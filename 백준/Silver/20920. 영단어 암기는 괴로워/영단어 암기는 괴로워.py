import sys
input = sys.stdin.readline

from collections import Counter
n , m = map(int, input().split())
words =[]
for _ in range(n):
    words.append(str(input())[:-1])

eli_words = []
for word in words:
    if len(word) >= m:
        eli_words.append(word)
counter = Counter(eli_words)

sorted_dict = dict(sorted(counter.items(), key = lambda x: (-x[1], -len(x[0]), x[0])))

for dict in sorted_dict:
    print(dict)