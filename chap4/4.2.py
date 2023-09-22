"""
O (N) となる．詳しくは本のフィボナッチのメモ化図をイメージ
for を使った場合は，単純な動的計画法となるが，これは「再帰＋メモ化」の動的計画法．ただし，オーダーは同じ．
"""
class tribo():
    
    def __init__(self, n):
        assert n >= 0
        if n <= 2:
            n = 2
        self.n = n
        self.memo = [-1] * (n + 1)
        self.memo[0] = 0
        self.memo[1] = 0
        self.memo[2] = 1
        
    def run(self, n):
        assert n <= self.n
        if self.memo[n] != -1:
            return self.memo[n]
        else:
            self.memo[n] = self.run(n-1) + self.run(n-2) + self.run(n-3)
            return self.memo[n]


if __name__ == '__main__':
    t = tribo(30)
    result = t.run(30)
    print(result)
    