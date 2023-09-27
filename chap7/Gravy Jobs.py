"""
問題文
ABC 君にお仕事の依頼が N 件来ました。各仕事には 1,2,⋯,N と番号が付けられています。
仕事 i は締切が 
Di日目の終わりであり、連続する Ci 日間を使うことで完了できます。
それ以外の方法で仕事を完了することはできません。より正確には、仕事i を締切までに完了するためには、
Ci ≤ k ≤ Di を満たすある整数 k について k−C i+1 日目の始めから k 日目の終わりまで i 番目の仕事を続けなければなりません。
仕事 i を締切までに完了するとSi円の報酬がもらえます。
1 日には高々1 種類しか仕事を行うことができません。
現在は 1 日目の始まりです。ABC 君が上手く取り掛かる仕事を選んでスケジュールを組んだ場合、彼が得られる報酬の金額として考えられる最大値を求めてください。
"""
# ステップごとに，各dayまでで最大のものを選択していく．
# この dp はworkが締め切り順であることが前提．なぜなら，各ワークの締め切り基準にを取るか，取らないかで各ステップの最大値を求めているから，後から前の締め切りの条件を追加されると困る．
#    0, 1, 2, 3, ... (day)
# 0, 0, 0, 0, 0, ...
# 1, 0,
# 2, 0,
# ...
# (work)
import numpy as np
np.set_printoptions(threshold=10000)

if __name__ == '__main__':
    N = int(input())
    DCS = [list(map(int, input().split())) for _ in range(N)]
    DCS = sorted(DCS, key=lambda x: (x[0], -x[2]))

    deadline = DCS[-1][0]
    dp = [[0]*(deadline+1) for _ in range(N+1)]
    
    for i, (d, c, s) in enumerate(DCS, start=1):
        for j in range(1, deadline+1):
            if d >= j >= c:
                dp[i][j] = max(dp[i-1][j-c]+s, dp[i-1][j])  # iの仕事を捨てずに，c日前の最大値と仕事のスコアを加算 or 仕事iをすてて，その日までの最大値を得る．
            elif c > j:     # 日付が足りない場合
                assert i-1 >= 0
                dp[i][j] = dp[i-1][j]
            elif j > d:     # 見ている範囲が締め切りを超した場合．
                assert i-1 >= 0
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # 取り出すのは，最終日ではなく
    print(dp[-1][-1])
