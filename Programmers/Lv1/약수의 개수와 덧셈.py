def count(n):
    return len([i for i in range(1, n//2+1) if n%i==0])+1
def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        if count(i) % 2 == 0:
            print(i)
            sum += i
        else:
            sum -= i
    return sum

solution(13,17)