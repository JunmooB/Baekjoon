import sys
input = sys.stdin.readline


tanos = list(input()[:-1])
zero_cnt = tanos.count('0')
one_cnt = tanos.count('1')

for _ in range(one_cnt//2):
    tanos.remove('1')
tanos.reverse()
for _ in range(zero_cnt//2):
    tanos.remove('0')
tanos.reverse()

for text in tanos:
    print(text, end='')