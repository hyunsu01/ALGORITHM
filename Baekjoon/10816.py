# 10816_숫자 카드2

N = int(input())
cards = [*map(int, input().split())]

M = int(input())
check = [*map(int, input().split())]

count = {}
for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in check:
    if i in count:
        print(count[i], end = ' ')
    else:
        print(0, end = ' ')
