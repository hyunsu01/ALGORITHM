# 좌표 압축 - 이진탐색
import sys
N = int(sys.stdin.readline())
nums = [*map(int, sys.stdin.readline().split())]
arr = sorted(set(nums))
# print(nums)

dic = {arr[i] : i for i in range(len(arr))}
for i in nums:
    print(dic[i], end = ' ')