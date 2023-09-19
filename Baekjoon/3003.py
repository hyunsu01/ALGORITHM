# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰

king, queen, rook, bishop, knight, pawn = map(int, input().split())
k, q, r, b, kn, p = 1, 1, 2, 2, 2, 8
print(k - king, q - queen, r - rook, b - bishop, kn - knight, p - pawn)
