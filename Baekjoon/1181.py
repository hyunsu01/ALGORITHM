# 1181. 단어정렬
N = int(input())
arr = []
for _ in range(N):
    word = input()
    arr.append(word)
words = sorted(arr, key=lambda x: (len(x), x))
for word in words:
    print(word)