def solution(N, stages):
    stages.sort()
    answer = []
    total_players = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if total_players == 0:
            fail = 0
        else:
            fail = count / total_players
        answer.append((i, fail))
        total_players -= count
    count = 0

    # 실패율을 기준으로 내림차순 정렬
    answer.sort(key=lambda x: x[1], reverse=True)
    # 스테이지 번호만 추출하여 answer 리스트에 저장
    answer = [num[0] for num in answer]
    print(answer)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)