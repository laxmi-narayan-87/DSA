class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])-1
        mainRow=[]
        for i in range(len(matrix)):
            if target<= matrix[i][n]:
                mainRow=matrix[i]
                break
        for j in range(len(mainRow)):
            if target==mainRow[j]:
                return True
        else:
            return False