class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row=len(grid)
        cols=len(grid[0])
        total=sum(sum(row) for row in grid)
        if total%2 !=0:
            return False
        target=total//2
        colsum=0
        for i in range(cols-1):
            for j in range(row):
                colsum+=grid[j][i]
            if colsum==target:
                return True
        rowsum=0
        for j in range(row-1):
            for i in range(cols):
                rowsum+=grid[j][i]
            if rowsum==target:
                return True
        return False