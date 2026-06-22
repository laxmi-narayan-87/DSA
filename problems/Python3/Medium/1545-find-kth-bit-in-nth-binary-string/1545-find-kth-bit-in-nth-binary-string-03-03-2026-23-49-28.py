class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse_and_inverse(s):
            s.reverse()
            s = [1 if c == 0 else 0 for c in s]
            return s
        res = [0]
        for i in range(1, n):
            res = res + [1] + reverse_and_inverse(res)
            if len(res) > k - 1:
                return str(res[k - 1])
        return str(res[k - 1])