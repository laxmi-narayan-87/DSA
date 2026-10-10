class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        change=False
        elaptime=0
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        def issafe(i,j,n,m):
            return 0<=i<n and 0<=j<m
        while True:
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==elaptime +2:
                        for dir in direction:
                            x= i+dir[0]
                            y=j+dir[1]
                            if issafe(x,y,n,m) and grid[x][y]==1:
                                grid[x][y]= grid[i][j]+1
                                change= True 
            if not change:
                break
            change= False
            elaptime +=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return elaptime