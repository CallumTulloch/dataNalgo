"""
相違なる数字 => setが使える．
"""

#N, M = map(int, input().split())
#A = input().split()
#B = input()

N = 1000000
M = 1000000
A = list(map(str, range(N)))
B = list(map(str, range(50, 50+N)))

cnt = 0
sets = set(A)
for b in B:
    if b in sets:
        cnt += 1
print(cnt)