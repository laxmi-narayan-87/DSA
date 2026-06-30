class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        while len(repeated) < len(b):
            count += 1
            repeated += a
        if b in repeated:
            return count
        count += 1
        repeated += a
        if b in repeated:
            return count
        return -1