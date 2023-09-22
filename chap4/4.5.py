"""ポイント
1. 作ったものが条件を満たしているか判定する関数を作ることを考えれるか．
2. 再帰を考え付くか．
3. カウントを蓄えて行くことを思いつくか
"""
def main():
    n = int(input())
    m = len(str(n))
    def dfs(A):
        # nよりも大きくなったら0を返す
        if int(A) > n:
            return 0
        # 入力されたものが753数ならcnt=1としていく
        cnt = 1 if all(A.count(c) > 0 for c in '753') else 0
        # 実際に用件を満たすような文字列の出力
        if cnt == 1:
            print(A[1:])
        for i in '753':
            cnt += dfs(A + i)
        return cnt
    print('入力値', n, 'の753数は', dfs('0'))
    
if __name__ == '__main__':
    main()