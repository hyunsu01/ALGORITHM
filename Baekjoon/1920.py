# 수 찾기_이진탐색
import sys

def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
N_arr = sorted(N_arr)

M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))

for m in M_arr:
    result = binary_search(N_arr, m)
    print(result)