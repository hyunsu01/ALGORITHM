def solution(numbers):
    all_numbers = set(range(10))
    for num in numbers:
        all_numbers.remove(num)
    result = sum(all_numbers)
    return result