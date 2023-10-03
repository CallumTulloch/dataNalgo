"""
O(N)
"""
#N = int(input())
#A = input().split()
#B = input()
#K = input()

N = 10
K = 3
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
    a = K - int(b)
    try:
        print(a, len(dic[f'{a}']))
        cnt += len(dic[f'{a}'])
    except:
        continue
print(cnt)