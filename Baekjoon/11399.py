# ATM_그리드
N = int(input())
people = list(map(int, input().split()))
people = sorted(people)
plus = 0
answer = 0
for i in people:
    plus += i
    answer += plus
    
print(answer)