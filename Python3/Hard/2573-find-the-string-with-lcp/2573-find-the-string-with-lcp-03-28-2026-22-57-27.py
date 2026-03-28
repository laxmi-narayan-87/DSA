class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n=len(lcp)
        for i in range(n):
            if lcp[i][i]!=n-i:
                return ""
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)]=find(y)
        for i in range(n):
            for j in range(n):
                if lcp[i][j]>0:
                    union(i,j)
        charmap={}
        current=ord('a')
        res=['']*n
        for i in range(n):
            root=find(i)
            if root not in charmap:
                if current>ord('z'):
                    return ""
                charmap[root]=chr(current)
                current+=1
            res[i]=charmap[root]
        s="".join(res)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[j]:
                    if i+1 < n and j+1 < n:
                        dp[i][j] = dp[i+1][j+1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
                if dp[i][j] != lcp[i][j]:
                    return ""
        return s