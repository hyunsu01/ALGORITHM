def solution(my_string):
    remove_letters = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i not in remove_letters:
            answer += i
    return answer