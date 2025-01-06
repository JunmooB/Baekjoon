import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    word = str(input().strip())
    words.append(word)
cnt = 0
for word in words:
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        else:
            if word[i] in word[i+1:]:
                cnt += 1
                break
print(n - cnt)