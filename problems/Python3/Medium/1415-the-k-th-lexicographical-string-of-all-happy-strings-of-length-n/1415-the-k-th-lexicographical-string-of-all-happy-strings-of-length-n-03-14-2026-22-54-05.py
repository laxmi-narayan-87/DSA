class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n-1))
        if k > total:
            return ""
        chars = ['a','b','c']
        res = ""
        k -= 1
        block = 1 << (n-1)
        first = k // block
        res += chars[first]
        k %= block
        for i in range(1, n):
            block //= 2
            prev = res[-1]            
            options = [c for c in chars if c != prev]
            idx = k // block
            res += options[idx]
            k %= block
        return res