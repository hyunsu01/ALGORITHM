def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)): 
        if signs[i]: #signs[i]인 경우 true
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    return sum

solution([4,7,12],['true','false','true'])