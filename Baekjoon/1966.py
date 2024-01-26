# 프린터 큐 - 큐
K = int(input())
for _ in range(K):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    count = 0
    while array:
        if array[0] < max(array):
            array.append(array.pop(0))
        else:
            count += 1
            array.pop(0)
            if M == 0:
                print(count)
                break            
        if M > 0:
            M -= 1
        else:
            M = len(array) - 1