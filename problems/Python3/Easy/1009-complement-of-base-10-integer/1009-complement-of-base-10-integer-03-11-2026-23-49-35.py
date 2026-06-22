class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        res = ""
        for ch in b:
            if ch == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)