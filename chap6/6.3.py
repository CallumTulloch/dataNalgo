import bisect

def main():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(N)]
    P.append(0)
    
    S = []
    for i in P:
        for j in P:
            S.append(i + j)
    
    S.sort()
    
    res = 0
    for a in S:
        idx = bisect.bisect_right(S, M-a)  # upper_boundのPythonバージョン
        if idx == 0:
            continue
        res = max(res, a + S[idx-1])
    
    print(res)

if __name__ == "__main__":
    main()