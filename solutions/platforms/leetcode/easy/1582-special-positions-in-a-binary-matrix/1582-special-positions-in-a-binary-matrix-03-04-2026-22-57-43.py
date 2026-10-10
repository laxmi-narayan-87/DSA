class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count={}
        col_count={}
        ones=[]
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    ones.append((i,j))
                    row_count[i]=row_count.get(i,0)+1
                    col_count[j]=col_count.get(j,0)+1
        ans=0
        for i,j in ones:
            if row_count[i]==1 and col_count[j]==1:
                ans+=1
        return ans