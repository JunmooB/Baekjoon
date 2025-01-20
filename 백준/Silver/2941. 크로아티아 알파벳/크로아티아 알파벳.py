import sys
input = sys.stdin.readline

croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = str(input().strip())

for crotia in croatia_list:
    text = text.replace(crotia, '#')
print(len(text))   