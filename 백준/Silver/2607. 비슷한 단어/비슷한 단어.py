import sys
input = sys.stdin.readline


n = int(input())
raw_word = list(input())
result = 0

for _ in range(n-1):
    word = raw_word.copy()
    exam = list(input())
    
    word.sort()
    exam.sort()

    if word == exam:
        result += 1

    elif (len(word) == len(exam) + 1) or (len(word) == len(exam)):
        for ex in exam:
            if ex in word:
                word.remove(ex)
        if len(word) == 1:
            result += 1

    elif len(word) == len(exam) - 1:
        for wo in word:
            if wo in exam:
                exam.remove(wo)
        if len(exam) == 1:
            result += 1
    else:
        continue
print(result)
