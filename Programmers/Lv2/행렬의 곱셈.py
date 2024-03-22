def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)): # arr1 헹의 개수
        arr = arr1[i]
        column = []
        for j in range(len(arr2[0])): # arr2 열의 개수
            sum = 0
            for k in range(len(arr1[0])): # arr1 열의 개수
                sum += arr[k] * arr2[k][j]
            column.append(sum)
        answer.append(column)
    # print(answer)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
solution(arr1, arr2)