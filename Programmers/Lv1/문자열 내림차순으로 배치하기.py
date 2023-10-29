def solution(s):
    s = ''.join(sorted(s, reverse=True))
    print(s)
    return s

solution("Zbcdefg")
