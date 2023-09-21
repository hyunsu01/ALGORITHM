# 5341. Pyramids
N = int(input())
arr = []
while N != 0:
    arr.append(N)
    N = int(input())
# print(arr)
for n in arr:
    print(sum(i for i in range(1, n+1)))