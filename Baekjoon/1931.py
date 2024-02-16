# 회의실 배정_그리디
import sys
N = int(sys.stdin.readline())
count = 0
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# end_x[1]을 오름차순 정렬한 후 start_x[0] 오름차순 정렬
arr.sort(key=lambda x: (x[1], x[0]))
end_time = 0

for meeting in arr:
    start, end = meeting[0], meeting[1]
    if start >= end_time:
        end_time = end
        count += 1

print(count)