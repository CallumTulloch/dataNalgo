"""
O(N+M)
相違でない数字 => dictを用いる
"""
#N, M = map(int, input().split())
#A = input().split()
#B = input()

#N = 1000000
#M = 1000000
#A = list(map(str, range(N)))
#B = list(map(str, range(50, 50+N)))

N = 10
M = 10
A = ['0', '1', '1', '2', '2', '2', '3', '3', '3', '3']
B = ['0', '1', '1', '2', '2', '2', '3', '3', '3', '3']

cnt = 0
dic = {}
for i, a in enumerate(A):
    try:
        dic[a].append(i)
    except:
        dic[a] = [i]

for i, b in enumerate(B):
    try:
        cnt += len(dic[b])
    except:
        continue
print(cnt)