def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    result = []

    for i in range(len(answers)):
        if first[i % 5] == answers[i]:
            count[0] += 1
        if second[i % 8] == answers[i]:
            count[1] += 1
        if third[i % 10] == answers[i]:
            count[2] += 1
    # print(count)

    for idx, val in enumerate(count):
        if val == max(count):
            result.append(idx+1)
    # print(result)
    return result

solution([1,2,3,4,5])
solution([1,3,2,4,2])