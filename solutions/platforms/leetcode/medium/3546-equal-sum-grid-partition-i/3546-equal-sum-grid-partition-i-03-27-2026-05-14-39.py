class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row,col=len(grid),len(grid[0])
        total=sum(sum(i) for i in grid)
        if total % 2:
            return False
        target=total//2
        colsum=[0]*col
        for i in range(row):
            for j in range(col):
                colsum[j]+=grid[i][j]
        prefix=0
        for j in range(col-1):
            prefix+=colsum[j]
            if prefix==target:
                return True
        prefix=0
        for i in range(row-1):
            prefix+=sum(grid[i])
            if prefix==target:
                return True
        return False