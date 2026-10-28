class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        time=0
        change=False
        direc=[[1,0],[0,1],[-1,0],[0,-1]]
        def isfresh(i,j,m,n):
            return 0<=i<m and 0<=j<n
        while True:
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==time+2:
                        for dir in direc:
                            x=i+dir[0]
                            y=j+dir[1]
                            if isfresh(x,y,m,n) and grid[x][y]==1:
                                grid[x][y]=grid[i][j]+1
                                change=True
            if not change:
                break
            change=False
            time+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return time