def solution(box, n):
    width, height, depth = box
    return (width // n) * (height // n) * (depth // n)

print(solution([1, 1, 1], 1)) # 1
print(solution([10, 8, 6], 3)) # 12