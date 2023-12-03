def GCD(x, y):  # 최대공약수
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):  # 최소공배수
    return (x * y) // GCD(x, y)

def solution(n, m):
    return [GCD(n, m), LCM(n, m)]