class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        n=len(s1)
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)]=find(y)
        for i in range(2,n):
            union(i,i-2)
        groups =defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        for indices in groups.values():
            if sorted(s1[i]for i in indices) !=sorted(s2[i] for i in indices):
                return False
        return True