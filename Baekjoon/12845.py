# 모두의 마블_그리디
import sys
n = int(sys.stdin.readline())
levels = list(map(int, sys.stdin.readline().split()))
levels.sort(reverse=True)

gold = 0
high = levels[0]

for i in range(1,len(levels)):
    gold+=(high+levels[i])

print(gold)