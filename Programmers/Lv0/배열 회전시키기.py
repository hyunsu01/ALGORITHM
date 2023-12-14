def solution(numbers, direction):
    num = len(numbers)
    ans = []
    if direction == 'left':
        ans = numbers[1:]
        ans.append(numbers[0])
        # print(ans)
    else:
        ans = [numbers[num-1]] + numbers[0:num-1]
        # print(ans)
    return ans

solution([1, 2, 3],"right")
solution([4, 455, 6, 4, -1, 45, 6], "left")