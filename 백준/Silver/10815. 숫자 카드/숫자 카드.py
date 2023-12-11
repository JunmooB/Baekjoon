import sys
input = sys.stdin.readline

def binary_search(num_cards, search):
    left = 0
    right = len(num_cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_cards[mid] > search:
            right = mid - 1
        elif num_cards[mid] < search:
            left = mid + 1
        else:
            return 1
    return 0

n = int(input())
num_cards = list(map(int, input().split()))
num_cards.sort()

m = int(input())
search_cards = list(map(int, input().split()))

for search in search_cards:
    print(binary_search(num_cards, search), end=' ')