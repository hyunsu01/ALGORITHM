# ATM_그리디
N = int(input())
people = list(map(int, input().split()))
people = sorted(people)
plus = 0
answer = 0
for i in people:
    plus += i
    answer += plus
    
print(answer)