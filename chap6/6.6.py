import math

A, B, C = map(int, input().split())

INF = 10**16
l = 0
r = INF
y = 0
while 10**-6 <= abs(100 - y):
    mid = (r+l) / 2
    t = mid
    y = A * t + B * math.sin(C * t * math.pi)
    #print(y)
    if y == 100:
        #print(t)
        exit()
    elif y > 100:
        r = mid
    else:
        l = mid
print(t)