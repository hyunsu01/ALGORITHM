def solution(hp):
    count = 0
    if hp != 0:
        for i in (5,3,1):
            count += hp // i
            hp = hp % i

    print(count)
    return count

solution(23)
