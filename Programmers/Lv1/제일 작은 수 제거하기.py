def solution(arr):
    min_value = min(arr)
    arr.remove(min_value)
    if len(arr) == 0:
        return [-1]
    return arr
solution([4,3,2,1])
solution([10])