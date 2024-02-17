# 동전 0
import sys
n, k = map(int, input().split()) 
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
# arr.sort(reverse=True)
count = 0
for i in reversed(range(n)):
    count += k // arr[i] # 몫
    k = k % arr[i] # 나머지
print(count)