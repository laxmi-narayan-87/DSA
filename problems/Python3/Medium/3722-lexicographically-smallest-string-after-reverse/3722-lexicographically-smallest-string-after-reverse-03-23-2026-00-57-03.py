class Solution:
    def lexSmallest(self, s: str) -> str:
        n=len(s)
        smallest=s
        for i in range(1,n+1):
            cad=s[:i][::-1]+s[i:]
            smallest=min(cad,smallest)
            suf=s[:-i]+s[-i:][::-1]
            smallest=min(smallest,suf)
        return smallest
