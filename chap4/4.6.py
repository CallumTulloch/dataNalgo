"""
配列の用意の仕方は，動的計画法と同じ．
疑問：wをすべて求めなくてよい分，単純な動的計画法より早い？
    : このプログラムにおけるi,wは独立で，そもそもメモ化に意味はないのでは？-> 
ポイント：
選ぶ場合，選ばない場合のどちらもダメ → False
逆に言えば，どちらかがok ならTrue であり，1度Trueになると，ずっとTrueになることがイメージできるように．
"""

class f_rec():
    def __init__(self, a, w):
        self.a = a
        self.w = w
        self.memo = [[-1]*(w+1) for i in range(len(a)+1)]
    
    def run(self, i, w):
        if i == 0:
            if w == 0:
                self.memo[i][w] = True
                return True
            else:
                self.memo[i][w] = False
                return False
        # memoにあるか
        if self.memo[i][w] != -1:
            print('メモ利用', 'i=', i, 'w=', w, 'A[i]=', self.a[i])
            return self.memo[i][w]
        
        # 選ばない場合
        if self.run(i-1, w):
            self.memo[i][w] = True
            print('i =', i, 'w =', w, 'A[', i-1, ']=', self.a[i-1], 'を選ばない')
            return True
        
        # 選ぶ場合
        if self.run(i-1, w-self.a[i-1]):
            self.memo[i][w] = True
            print('i =', i, 'w =', w, 'A[', i-1, ']=', self.a[i-1], 'を選ぶ')
            return True
        
        self.memo[i][w] = False
        return False



if __name__ == '__main__':
    n, w = map(int, input().split())
    a = [int(x) for x in input().split()]
    
    f = f_rec(a, w)
    if f.run(n, w):
        print('Yes')
    else:
        print('No')