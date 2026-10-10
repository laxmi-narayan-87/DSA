class Solution:
    def minPartitions(self, n: str) -> int:
        # return int(max(n))
        max_digit="0"
        for d in n:
            if d>max_digit:
                max_digit=d
            if max_digit=="9":
                return 9
        return int(max_digit)