def solution(dirs):
    arr =  set()
    x, y = 0, 0 
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    count = 0
    for dir in dirs:
        dx, dy = moves[dir]
        new_x, new_y = x + dx, y + dy
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            arr.add(((x, y), (new_x, new_y)))
            arr.add(((new_x, new_y), (x, y)))
            x, y = new_x, new_y
    answer = len(arr) // 2
    # print(answer)
    return answer

dirs = "LULLLLLLU"
solution(dirs)