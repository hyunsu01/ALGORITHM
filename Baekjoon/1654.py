# 랜선 자르기_이진탐색
import sys
def binary_search(arr, target):
    start, end = 1, max(arr)
    while start <= end :
        count = 0
        mid = (start + end) // 2
        for i in arr:
            count += (i // mid)
        if count >= target:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

K, N = map(int, sys.stdin.readline().split())
arr = []
for n in range(K):
    arr.append(int(sys.stdin.readline()))
binary_search(arr, N)