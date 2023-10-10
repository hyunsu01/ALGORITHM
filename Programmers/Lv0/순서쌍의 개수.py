# Lv0_순서쌍의 개수
def solution(n):
    count = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            count +=1 
    return count+1