# 나무 자르기 - 이진탐색
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in trees:
        if height > mid:
            total += height - mid
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)