# 30087. 진흥원 세미나

N = int(input())
arr = []
dic = {'204':'Algorithm', '207':'DataAnalysis', '302':'ArtificialIntelligence', 'B101':'CyberSecurity', '303':'Network', '501':'Startup', '105':'TestStrategy'}

for _ in range(N):
    arr.append(input())

bb = {v: k for k, v in dic.items()}

for arr_val in arr:
    print(bb.get(arr_val))