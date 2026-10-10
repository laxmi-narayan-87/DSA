class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=len(matrix),len(matrix[0])
        first_row=any(matrix[0][j]==0 for j in range(col))
        first_col=any(matrix[i][0]==0 for i in range(row))

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            if matrix[i][0]==0:
                for j in range(1,col):
                    matrix[i][j]=0
        for j in range(1,col):
            if matrix[0][j]==0:
                for i in range(1,row):
                    matrix[i][j]=0
        if first_row:
            for j in range(col):
                matrix[0][j]=0
        if first_col:
            for  i in range(row):
                matrix[i][0]=0
