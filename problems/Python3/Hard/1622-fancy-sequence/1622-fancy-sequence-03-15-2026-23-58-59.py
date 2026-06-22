class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        val = (val - self.add) % self.MOD
        val = val * pow(self.mul, -1, self.MOD) % self.MOD
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)