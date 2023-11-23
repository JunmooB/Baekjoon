import sys
input = sys.stdin.readline

vowel = ['a','e','i','o','u']
double_vowel = ['ee', 'oo']

while True:
    result = True
    passwords = str(input())
    passwords = passwords[:len(passwords)-1]
    if passwords == "end":
        break

    # 모음 하나 포함
    cnt = 0 
    for vow in vowel:
        if vow in passwords:
            cnt +=1        
    if cnt == 0:
        result = False


    # 자음 3개 연속
    for i in range(len(passwords)-2):
        if not passwords[i] in vowel:
            if not passwords[i+1] in vowel:
                if not passwords[i+2] in vowel:
                    result = False
                    break
        # 모음 3개 연속
        if passwords[i] in vowel:
            if passwords[i+1] in vowel:
                if passwords[i+2] in vowel:
                    result = False
                    break
    # 같은 글자
    for i in range(len(passwords)-1):        
        if passwords[i] == passwords[i+1]:
            if (passwords[i] != 'e') and (passwords[i] != 'o'):
                result = False
                break
            
    if result:
        print(f"<{passwords}>", end='' )
        print(" is acceptable.")
    else:
        print(f"<{passwords}>", end='' )
        print(" is not acceptable.")