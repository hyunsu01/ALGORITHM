def solution(numbers):
    ans = 1
    for i in range(2):
        max_num = max(numbers)
        # print(max_num)
        numbers.remove(max_num)
        ans *= max_num
    return ans

solution([1, 2, 3, 4, 5])