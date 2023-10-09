# Lv0_외계행성의 나이
def solution(age):
    dic = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f',
            '6':'g', '7':'h', '8':'i', '9':'j'}
    
    for i in str(age):
        answer+=(dic[i])
    return answer