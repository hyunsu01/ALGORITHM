def solution(emergency):
    sort_e = sorted(emergency, reverse=True)
    answer = []
    for e in emergency:
        index = sort_e.index(e) + 1
        answer.append(index)
    return answer